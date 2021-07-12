#
# Copyright 2020 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'supported_by': 'community',
    'status': ['preview']
}

DOCUMENTATION = """
---
module: demo_module

"""

EXAMPLES = """
- demo_module
"""

RETURN = """
demo module retur
"""

from ansible.module_utils.basic import AnsibleModule
import re



def main():
    """Ansible module to verify IP reachability using Ping RPC over NETCONF."""
    module = AnsibleModule(
        argument_spec=dict(
            var1=dict(type='dict', required=True)
        ),
        supports_check_mode=True
    )

    f= open("04-config-aditional.cfg", "w")
    for old_map, new_map in module.params['var1'].items():
        if not "tbd" in old_map:
            speed_var=re.findall(r'([0-9]+)Mbps',new_map)[0]
            pm_var = f"""policy-map {speed_var}Mbps-IN
 class class-default
  police rate {speed_var} mbps
   conform-action set precedence 0
   exceed-action drop
  !
!
 end-policy-map
!
"""
            f.write(pm_var)
    f.close()
    if module.check_mode:
        module.exit_json(changed=False)

    module.exit_json(meta="04-config-aditional.cfg")


if __name__ == '__main__':
    """Execute main program."""
    main()

# End of module
