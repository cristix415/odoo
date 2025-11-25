/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

class CAQ3Home extends Component {
    static template = "CAQ3HomeTemplate";  // numele template-ului din XML
}

registry.category("actions").add("caq3_home", CAQ3Home);
