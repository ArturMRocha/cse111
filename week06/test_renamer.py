

import pytest
from pathlib import Path


from renamer import find_files_in_directory, build_batch_rename_map

def test_find_files_in_directory(tmp_path: Path):
    """Tests the file finding function."""

    (tmp_path / "photo.jpg").touch()
    (tmp_path / "document.pdf").touch()
    (tmp_path / "renamer.py").touch() 
    
    ignore_list = ['renamer.py', 'test_renamer.py'] 
    

    result = find_files_in_directory(tmp_path, ignore_list)
    result_names = {p.name for p in result}
    
    
    assert len(result) == 2
    assert "photo.jpg" in result_names
    assert "renamer.py" not in result_names 

def test_build_batch_rename_map(tmp_path: Path):
    """Tests the rename map creation for batch mode."""
   
    file_list = [tmp_path / 'a.txt', tmp_path / 'b.png']
    test_prefix = "Project_Alpha"
    
   
    result_map = build_batch_rename_map(file_list, test_prefix)
    

    assert len(result_map) == 2

    expected_new_path_1 = tmp_path / "Project_Alpha_1.txt"
    expected_new_path_2 = tmp_path / "Project_Alpha_2.png"
    
    assert result_map[tmp_path / 'a.txt'] == expected_new_path_1
    assert result_map[tmp_path / 'b.png'] == expected_new_path_2