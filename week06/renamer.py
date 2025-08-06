

import os
from pathlib import Path
import math

def find_files_in_directory(directory: Path, ignore_list: list[str]) -> list[Path]:
    """Finds all files in a directory, excluding specified names."""
    if not directory.is_dir():
        return []
    files = [f for f in directory.iterdir() if f.is_file() and f.name not in ignore_list]
    files.sort()
    return files

def build_batch_rename_map(files_list: list[Path], prefix: str) -> dict[Path, Path]:
    """Builds a rename map for BATCH mode (prefix + sequential number)."""
    rename_map = {}
    if not files_list:
        return rename_map
    
    padding = math.ceil(math.log10(len(files_list) + 1))
    
    for i, old_path in enumerate(files_list):
        new_name_str = f"{prefix}_{i + 1:0{padding}d}{old_path.suffix}"
        new_path = old_path.with_name(new_name_str)
        rename_map[old_path] = new_path
    return rename_map

def execute_rename_operation(rename_map: dict[Path, Path]):
    """Executes the actual file renaming based on the map."""
    print("\n🚀 Starting rename operation...")
    success_count = 0
    for old, new in rename_map.items():
        try:
            os.rename(old, new)
            print(f"  ✅ SUCCESS: {old.name} -> {new.name}")
            success_count += 1
        except OSError as e:
            print(f"  ❌ ERROR renaming {old.name}: {e}")
    print(f"\n✨ Operation complete! {success_count} files were successfully renamed.")


# --- Main Application Logic with Improved User Interface ---

def main():
    """Main function to drive the user interaction and renaming process."""
    print("="*60)
    print("      Master Batch File Renamer and Organizer") # <-- ALTERAÇÃO AQUI: v4.0 removido
    print("="*60)
    
    # Step 1: Find the target folder
    input_str = input("▶ Enter the folder name to search (e.g., wallpaper) or a full path: ")
    target_dir = None
    potential_path = Path(input_str)

    if potential_path.is_dir():
        target_dir = potential_path
    else:
        print(f"\n🔍 Searching for a folder named '{input_str}' in your personal files...")
        home_dir = Path.home()
        found_folders = [p for p in home_dir.rglob(input_str) if p.is_dir() and p.name == input_str]
        
        if not found_folders:
            print(f"\n❌ ERROR: No folder named '{input_str}' was found. Please try again.")
            return
        elif len(found_folders) == 1:
            target_dir = found_folders[0]
            print(f"✔️ Folder found at: {target_dir.resolve()}")
        else:
            print("\n⚠️ Multiple folders found. Please choose one:")
            for i, folder in enumerate(found_folders):
                print(f"  [{i + 1}] {folder.resolve()}")
            while True:
                try:
                    choice = int(input("Enter the number of the folder you want to use: ")) - 1
                    if 0 <= choice < len(found_folders):
                        target_dir = found_folders[choice]
                        break
                    else:
                        print("Invalid number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

    if not target_dir:
        print("No valid folder selected. Exiting.")
        return

    # Step 2: List files and let the user select which ones to process
    ignore_list = ['renamer.py', 'test_renamer.py'] # <-- ALTERAÇÃO AQUI: nome do arquivo ajustado
    all_files = find_files_in_directory(target_dir, ignore_list)
    
    if not all_files:
        print("\nNo files available to rename in this folder.")
        return
        
    print("\n📄 Files found in the folder:")
    for i, file_path in enumerate(all_files):
        print(f"  [{i + 1}] {file_path.name}")
    
    while True:
        mode = input("\nRename [A]ll files or [C]hoose specific ones? (A/C): ").upper()
        if mode in ['A', 'C']:
            break
        print("Invalid option. Please enter 'A' or 'C'.")
    
    files_to_process = []
    if mode == 'A':
        files_to_process = all_files
    elif mode == 'C':
        while True:
            try:
                numbers_str = input("Enter the file numbers, separated by commas (e.g., 1, 3, 5): ")
                selected_indices = [int(n.strip()) - 1 for n in numbers_str.split(',')]
                files_to_process = [all_files[i] for i in selected_indices if 0 <= i < len(all_files)]
                if files_to_process:
                    break
                else:
                    print("No valid files selected. Please check the numbers.")
            except ValueError:
                print("Invalid input. Please enter numbers separated by commas.")

    if not files_to_process:
        print("No files selected to process. Exiting.")
        return
        
    # Step 3: Choose rename mode (Batch or Individual)
    while True:
        rename_mode = input("\nHow do you want to rename?\n  [B]atch mode (e.g., Prefix_01, Prefix_02)\n  [I]ndividual mode (a unique name for each file)\n(B/I): ").upper()
        if rename_mode in ['B', 'I']:
            break
        print("Invalid option. Please enter 'B' or 'I'.")
    
    rename_map = {}
    if rename_mode == 'B':
        default_prefix = target_dir.resolve().name.replace(' ', '_')
        prefix_input = input(f"\nEnter a prefix for the new files (press Enter to use '{default_prefix}'): ")
        prefix = prefix_input or default_prefix
        rename_map = build_batch_rename_map(files_to_process, prefix)
    elif rename_mode == 'I':
        print("\n--- Individual Renaming Mode ---")
        for file_path in files_to_process:
            new_name_base = input(f"  New name for '{file_path.name}' (without extension): ")
            if new_name_base:
                new_path = file_path.with_name(new_name_base + file_path.suffix)
                rename_map[file_path] = new_path
            else:
                print("    -> Skipped (name was empty).")

    if not rename_map:
        print("\nNo changes to be made. Operation finished.")
        return

    # Final Step: Preview and Confirmation
    print("\n" + "="*25 + " PREVIEW " + "="*26)
    for old, new in rename_map.items():
        print(f"  {old.name}  ->  {new.name}")
    print("="*60)
    
    try:
        confirm = input(f"Are you sure you want to rename these {len(rename_map)} file(s)? (yes/no): ")
    except EOFError:
        confirm = 'no'
        
    if confirm.lower() == 'yes':
        execute_rename_operation(rename_map)
    else:
        print("\nOperation cancelled by user.")


if __name__ == "__main__":
    main()