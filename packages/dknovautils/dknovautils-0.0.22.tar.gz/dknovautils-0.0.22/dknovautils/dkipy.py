from dknovautils.dkat import AT


class DkIpyUtils(object):

    # class attribute

    @staticmethod
    def mfc(cmd: str):
        assert isinstance(cmd, str) and len(cmd) > 0, 'err3581'
        AT.unimplemented()

    @staticmethod
    def mfr(cmd) -> any:
        AT.unimplemented()
        return None
    

def dk_mfc(cmd): DkIpyUtils.mfc(cmd)

def dk_mfr(cmd): return DkIpyUtils.mfr(cmd)
