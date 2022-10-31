import hashlib
import pytest
from slimebox import Slime, Color, clamp, mix_colors
import sim

def test_case2(capsys):
    sim.main('case2.input')
    captured = capsys.readouterr()
    assert hashlib.sha256(captured.out.strip().encode('utf_8')).hexdigest() == 'e3db407a9099d5f8d608ef40af14f5ca16cccf332c93150d03ac3d041747d860'

def test_case3(capsys):
    sim.main('case3.input')
    captured = capsys.readouterr()
    assert hashlib.sha256(captured.out.strip().encode('utf_8')).hexdigest() == '797537f648c57488d72c5fbcd3730c7a452ecf3fc269e82df4f21703b7d36df1'


