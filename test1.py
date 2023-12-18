import os

def test_config_file_exists():
    assert os.path.isfile('/home/config.txt'), "config.txt not found in /home"
    print("config.txt found in /home")

def test_joki_file_exists():
    assert os.path.isfile('/home/joki.py'), "joki.py not found in /home"
    print("joki.py found in /home")

def test_skript_file_exists():
    assert os.path.isfile('/home/skript.py'), "skript.py not found at /home"
    print("skript.py found at /home")

def test_db_config_in_skript():
    skript_path = '/home/skript.py'
    assert os.path.isfile(skript_path), f"{skript_path} not found at /home"
    
    with open(skript_path, 'r') as file:
        content = file.read()
        assert 'db_config' in content, "db_config not found in skript.py"
    
    print("db_config found in skript.py")
