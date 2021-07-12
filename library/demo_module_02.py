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


def main():
    """Ansible module to verify IP reachability using Ping RPC over NETCONF."""
    module = AnsibleModule(
        argument_spec=dict(
            var1=dict(type='dict', required=True)
        ),
        supports_check_mode=True
    )

    dic_temp = module.params['var1']
    for i in dic_temp.keys():
        in_new = module.params['var1'][i]['in_new']
        in_old = module.params['var1'][i]['in_old']
        dic_temp[i]['in_old'] = in_new
        dic_temp[i]['in_new'] = in_old
        out_new = module.params['var1'][i]['out_new']
        out_old = module.params['var1'][i]['out_old']
        dic_temp[i]['out_old'] = out_new
        dic_temp[i]['out_new'] = out_old


    if module.check_mode:
        module.exit_json(changed=False)

    module.exit_json(meta=dic_temp)


if __name__ == '__main__':
    """Execute main program."""
    main()

# End of module
