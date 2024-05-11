import os
import sys

# Check if the current working directory is not the script directory

if __name__ == "services":
    if os.getcwd() != os.path.dirname(__file__):
        # Create a path to the 'services' directory within the current working directory
        # services_path = os.path.join(current_working_directory, 'services')

        sys.path.append(os.path.abspath('services'))
    from Argument_service import argument_Set

    
    __arg = argument_Set(description="Set system run basic กำหนดการทำงาน เบื่องต้นของ programe ผ่าน command")

    __arg.argument_add(flags=['-t', '--test'],default="basic"
                    )
    __arg.argument_add(flags="manage_data",
                    help_description=" [default local] -> กำหนดให้ dataset แบบ local [load] -> Load new data from api respone", choices=["local", "load"], default="local")
    # arg = arg.parser.parse_args()
    arg = __arg.argument_create()

    print(arg.manage_data)
