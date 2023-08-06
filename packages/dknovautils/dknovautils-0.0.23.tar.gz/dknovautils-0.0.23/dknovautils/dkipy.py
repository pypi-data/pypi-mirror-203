from dknovautils.dkat import AT

from IPython.core.getipython import get_ipython


# a = get_ipython().getoutput('pwd')


class DkIpyUtils(object):

    # class attribute

    @staticmethod
    def mfc(cmd: str):
        DkIpyUtils.mfr(cmd)
        # assert isinstance(cmd, str) and len(cmd) > 0, 'err3581'
        # get_ipython().getoutput(cmd)
        # # AT.unimplemented()

    @staticmethod
    def mfr(cmd) -> any:
        assert isinstance(cmd, str) and len(cmd) > 0, 'err3581'
        r = get_ipython().getoutput(cmd)
        return r


def dk_mfc(cmd): DkIpyUtils.mfc(cmd)


def dk_mfr(cmd): return DkIpyUtils.mfr(cmd)

'''

!{cmd}

r=get_ipython().getoutput('{cmd}')



不能用 %cd 格式化会出错 用 os.chdir()

不用 echo 用 iprint






'''
