import os
import shutil
from dsc.repository import DistributedSourceControl

def setup_module(module):
    """Setup test environment."""
    if os.path.exists(".myrepo"):
        shutil.rmtree(".myrepo")

def teardown_module(module):
    """Clean up test environment."""
    if os.path.exists(".myrepo"):
        shutil.rmtree(".myrepo")

def test_init():
    result = DistributedSourceControl.init()
    assert result == "Initialized empty repository."
    assert os.path.exists(".myrepo")

def test_add():
    with open("testfile.txt", "w") as f:
        f.write("Test content")
    DistributedSourceControl.init()
    result = DistributedSourceControl.add("testfile.txt")
    assert result == "Staged file: testfile.txt"
    assert os.path.exists(".myrepo/staged/testfile.txt")
    os.remove("testfile.txt")

def test_commit():
    with open("testfile.txt", "w") as f:
        f.write("Test content")
    DistributedSourceControl.init()
    DistributedSourceControl.add("testfile.txt")
    result = DistributedSourceControl.commit("Test commit")
    assert "Committed changes:" in result
    assert len(os.listdir(".myrepo/commits")) > 0
    os.remove("testfile.txt")

def test_log():
    DistributedSourceControl.init()
    DistributedSourceControl.add("testfile.txt")
    DistributedSourceControl.commit("Test commit")
    result = DistributedSourceControl.log()
    assert "Test commit" in result
