#!/usr/bin/env python3
####################################################################################################
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
# Authors: Mason Remy
# Requires: Python 3.5+
####################################################################################################

import os

__script_path = os.path.dirname(os.path.abspath(__file__))
bin_dir = __script_path # Assume this script is deployed into the install bin dir
root_dir = os.path.abspath(os.path.join(__script_path, os.pardir))

class BuildConfig:
    c_compiler = r""
    cxx_compiler = r"C:/Program Files/Microsoft Visual Studio/2022/Enterprise/VC/Tools/MSVC/14.34.31933/bin/HostX64/x64/cl.exe"
    llvm_symbolizer = r"C:/Users/VssAdministrator/.conan/data/AcceraLLVM/llvmorg-15-24a37a396a9b/admin/stable/package/0a420ff5c47119e668867cdb51baff0eca1fdb68/bin/llvm-symbolizer.exe"
    llvm_custom_path = r""
    llvm_filecheck = r"C:/Users/VssAdministrator/.conan/data/AcceraLLVM/llvmorg-15-24a37a396a9b/admin/stable/package/0a420ff5c47119e668867cdb51baff0eca1fdb68/bin/FileCheck.exe"
    use_libcxx = r"OFF"
    config_in_build_path = True
    additional_cmake_init_args = r'-G "Visual Studio 17 2022" -A x64 -T host=x64'
    obj_extension = r".obj"
    asm_extension = r".s"
    static_library_extension = r".lib"
    static_library_prefix = r""
    shared_library_extension = r".dll"
    shared_library_prefix = r""
    exe_extension = r".exe"
    vulkan_runtime_wrapper_shared_library = os.path.join(root_dir, r"")
