odoo.define('web.test_AppSwitcher', function (require) {
 "use strict";

var session = require('web.session');
var AppSwitcher = require('web_enterprise.AppSwitcher');

session.expiration_date = false;
session.warning = false;

});
