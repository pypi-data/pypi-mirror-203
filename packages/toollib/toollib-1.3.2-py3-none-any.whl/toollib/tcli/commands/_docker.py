"""
@author axiner
@version v1.0.0
@created 2022/5/11 21:44
@abstract
@description
@history
"""
import json
import os
import re
import subprocess
import sys

from toollib.decorator import sys_required
from toollib.tcli import here
from toollib.tcli.base import BaseCmd
from toollib.tcli.option import Options, Arg


class Cmd(BaseCmd):

    def __init__(self):
        super().__init__()
        self.dkcmps_path = here.joinpath('commands', 'plugins', 'docker-compose.yml').as_posix()

    def add_options(self):
        options = Options(
            name='docker操作',
            desc='docker操作',
            optional={
                self.install: None,
                self.set_mirrors: None,
                self.compose: [
                    Arg('-n', '--names', required=True, type=str, help='镜像名称（多个用逗号隔开）'),
                    Arg('-o', '--outdir', type=str, help='输出目录'),
                    Arg('-f', '--filename', type=str, help='文件名称'),
                ],
                self.compose_list: None,
            }
        )
        return options

    @sys_required('centos|\.el\d|ubuntu', errmsg='仅支持centos|el|ubuntu')
    def install(self):
        cmd = 'curl -sSL https://get.daocloud.io/docker | sh'
        subprocess.run(cmd, shell=True)

    @sys_required('centos|\.el\d|ubuntu', errmsg='仅支持centos|el|ubuntu')
    def set_mirrors(self):
        mirrors = [
            "https://hub-mirror.c.163.com",
            "https://docker.mirrors.ustc.edu.cn",
            "https://registry.docker-cn.com",
        ]
        subprocess.run(['systemctl', 'stop', 'docker'])
        docker_etc_dir = '/etc/docker'
        if not os.path.isdir(docker_etc_dir):
            os.mkdir(docker_etc_dir)
        with open(os.path.join(docker_etc_dir, 'daemon.json'), 'w') as fp:
            fp.write('{"registry-mirrors": %s}' % json.dumps(mirrors))
        subprocess.run(['systemctl', 'start', 'docker'])

    def compose(self):
        names = self.parse_args.names
        outdir = self.parse_args.outdir
        if outdir:
            if not os.path.isdir(outdir):
                print(f'{outdir}: 目录不存在')
                sys.exit()
        else:
            outdir = os.getcwd()
        filename = self.parse_args.filename or 'docker-compose.yml'
        dkcmps_path = os.path.join(outdir, filename)
        wc = 0
        for name, dkcmps_conf in self._search_dkcmps_conf(names):
            if not dkcmps_conf:
                print(f'{name}: 抱歉暂未收录')
                self.compose_list()
            else:
                if os.path.isfile(dkcmps_path) and os.path.getsize(dkcmps_path):
                    with open(dkcmps_path, 'r') as fp:
                        if re.search(rf"\s\s{name}:\s*\r?\n", fp.read()):
                            print(f'{name}: `{dkcmps_path}`已经存在')
                            continue
                    mode = 'a'
                    dkcmps_conf = '\n\n' + dkcmps_conf
                else:
                    mode = 'w'
                    dkcmps_conf = 'version: "3"\nservices:\n\n' + dkcmps_conf
                with open(dkcmps_path, mode) as fp:
                    fp.write(dkcmps_conf)
                    print(f'{name}: `{dkcmps_path}`写入成功')
                    wc += 1
        if wc:
            print('后续可通过`docker-compose`命令管理容器（也可自行修改配置）')

    def _search_dkcmps_conf(self, names: str):
        with open(self.dkcmps_path, 'r') as fp:
            dkcmps_text = fp.read()
            if names == 'all':
                namelist = re.findall(r"^\s{2}(\w+):\s*\r?\n", dkcmps_text, re.MULTILINE)
            else:
                namelist = names.split(',')
            for n in namelist:
                regex = r'(\s{2}' + n + r':\s*.*?)(?=\r?\n\s*\r?\n|$)'
                matches = re.search(regex, dkcmps_text, re.DOTALL)
                if matches:
                    yield n, matches.group(0).rstrip()
                else:
                    yield n, None

    def compose_list(self):
        with open(self.dkcmps_path, 'r') as fp:
            namelist = re.findall(r"^(\s{2}\w+):\s*\r?\n", fp.read(), re.MULTILINE) or ['  正在努力收录中...']
            resp_text = '已收录的容器：\n' + '\n'.join(namelist)
            print(resp_text)
