from colorama import Fore, Style, init
init()
import importlib.util
import os

# user guide for making your own
# addon/addon2 will set replacee/replacement to a string. addon can be a list (optional), addon2 cant
# start_key/start_key2 will start the user in a json from a set position (make sure the set position doesnt share a name or ill go to the first one)
# return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names finishes an area and returns all the data back and finishes this codes use
# add a line push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names) for doing multiple changes of seperate things in the same case
# if you want to skip then set skip to True
# leaving empty and only returning will make the user enter 2 from the json starting from the top

def get_valid_input(prompt, valid_values=None):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'back':
            return 'back'
        try:
            if valid_values is None or int(user_input) in valid_values:
                return int(user_input)
            else:
                print(f"{Fore.RED}\nInvalid option. Please choose from {valid_values}.\n{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}\nInvalid input. Please enter a valid number.\n{Style.RESET_ALL}")


def push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names):
    spec = importlib.util.spec_from_file_location("backbone_module", "main.py")
    backbone_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(backbone_module)

    if hasattr(backbone_module, "backbone"):
        json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names = backbone_module.backbone(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
    else:
        print(f"Error: The file {backbone_module} does not contain a `backbone` function.")


def run(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names):

    while True:
        options = get_valid_input(f"Asset replacements:\n"
                        f"0:  {Fore.GREEN}Custom{Style.RESET_ALL}\n"
                        f"1:  {Fore.GREEN}Sights{Style.RESET_ALL}\n"
                        f"2:  {Fore.GREEN}Weapon Sounds{Style.RESET_ALL}\n"
                        f"3:  {Fore.GREEN}Hit sounds{Style.RESET_ALL}\n"
                        f"4:  {Fore.GREEN}No textures{Style.RESET_ALL}\n"
                        f"Type 'back' to return to the previous menu.\n: ",
                        valid_values=[0, 1, 2, 3, 4]
        )
        if options == 'back':
            print(f"{Fore.CYAN}\nReturning to main menu.{Style.RESET_ALL}")
            skip = True
            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
        
        try:
            match options:
                case 0:
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 1:
                    while True:
                        sight_option = get_valid_input(
                            f"\nEnter sight option:\n"
                            f"1: {Fore.GREEN}Reticle tweaks{Style.RESET_ALL}\n"
                            f"2: {Fore.GREEN}Sight model tweaks{Style.RESET_ALL}\n"
                            f"3: {Fore.GREEN}Ballistics tracker tweaks{Style.RESET_ALL}\n"
                            f"Type 'back' to return to the previous menu.\n: ",
                            valid_values=[1, 2, 3]
                        )
                        if sight_option == 'back':
                            print(f"{Fore.CYAN}\nReturning to Asset replacements.\n{Style.RESET_ALL}")
                            break

                        match sight_option:
                            case 1:
                                start_key = "reticles"
                                start_key2 = "reticle replacement"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 2:
                                while True:
                                    sightbackground = get_valid_input(
                                        f"\nEnter background tweak:\n"
                                        f"1: {Fore.GREEN}clear coyote blue background{Style.RESET_ALL}\n"
                                        f"2: {Fore.GREEN}clear reflex blue background{Style.RESET_ALL}\n"
                                        f"3: {Fore.GREEN}clear okp-7 blue background{Style.RESET_ALL}\n"
                                        f"4: {Fore.GREEN}clear delta black ring{Style.RESET_ALL}\n"
                                        f"5: {Fore.GREEN}remove sniper black circle{Style.RESET_ALL}\n"
                                        f"6: {Fore.GREEN}remove glass hack border{Style.RESET_ALL}\n"
                                        f"7: {Fore.GREEN}make oled good{Style.RESET_ALL}\n"
                                        f"Type 'back' to return to the previous menu.\n: ",
                                        valid_values=[1, 2, 3, 4, 5, 6, 7]
                                    )
                                    if sightbackground == 'back':
                                        print(f"{Fore.CYAN}\nReturning to sight options.{Style.RESET_ALL}")
                                        break

                                    match sightbackground:
                                        case 1:
                                            addon = "3fc9141fc7c1167c575b9361a98f04c0"
                                            addon2 = "5873cfba79134ecfec6658f559d8f320"
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 2:
                                            addon = "2eaae4fe3a9fce967af993d27ad68d52"
                                            addon2 = "5873cfba79134ecfec6658f559d8f320"
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 3:
                                            addon = "2eaae4fe3a9fce967af993d27ad68d52"
                                            addon2 = "5873cfba79134ecfec6658f559d8f320"
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 4:
                                            addon = ['30c4d2bb30b6b8c9ac7cfeec5db25a85', '7d5652167ec33ed349e569a55a398705']
                                            addon2 = "75205be5a167842c7ed931d9d5a904ca"
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 5:
                                            addon = ['a883a2373ad6931556dce946c50c3690', '5a2a41b0da7ec98bf25780bb3f5d071f']
                                            addon2 = "75205be5a167842c7ed931d9d5a904ca"
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 6:
                                            addon = '1764672fe43c9f1d129b3d51dc3c40ee'
                                            addon2 = '75205be5a167842c7ed931d9d5a904ca'
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 7:
                                            addon = '97d2da0d7a507151b10988ba762a7061'
                                            addon2 = 'bf8e63c3b7a7deeb0011a164c50f943f'
                                            push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                            addon = '0fd98b21b47dbd948988ec1c67696af8'
                                            addon2 = '5873cfba79134ecfec6658f559d8f320'
                                            push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                            addon = '009b0b998ae084f23e5c0d7b1f9431b3'
                                            addon2 = '577f6c95249ebea2926892c3f3e8c040'                                            
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names                                            
                            case 3:
                                addon = "0847bd551fe2cbe953a3c3670eac79b1"
                                start_key2 = "ballistics tracker"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 2:
                    while True:
                        arm_option = get_valid_input(
                            f"\nEnter arm option:\n"
                            f"1: {Fore.GREEN}Remove options{Style.RESET_ALL}\n"
                            f"2: {Fore.GREEN}Bone arms{Style.RESET_ALL}\n"
                            f"Type 'back' to return to the previous menu.\n: ",
                            valid_values=[1, 2]
                        )

                        if arm_option == 'back':
                            print(f"{Fore.CYAN}\nReturning to Asset replacements.\n{Style.RESET_ALL}")
                            break

                        match arm_option:
                            case 1:
                                start_key = "arm models"
                                addon2 = "5873cfba79134ecfec6658f559d8f320"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 2:
                                start_key = "bare arms"
                                addon2 = "5873cfba79134ecfec6658f559d8f320"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 3:
                    addon = "8813bbc8c0f7c0901fc38c1c85935fec"
                    start_key2 = "skins"
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 4:
                    start_key = "textures"
                    addon2 = "75205be5a167842c7ed931d9d5a904ca"
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
        except Exception as e:
            print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
