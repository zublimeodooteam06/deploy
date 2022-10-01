# -*- coding: utf-8 -*-
from odoo import models, fields

from odoo import api, fields, models


class GeneralSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _description = "url & secret key for bigbluebutton server"

    url = fields.Char(string="Url", config_parameter="big_blue_button_integration.url")
    secret_key = fields.Char(string="Secret Key", config_parameter="big_blue_button_integration.secret_key")
    logout_url = fields.Char(string="Logout Url", config_parameter="big_blue_button_integration.logout_url")

    def get_values(self):
        res = super(GeneralSettings, self).get_values()
        url = self.env["ir.config_parameter"].get_param(
            "url", default=None)
        secret_key = self.env["ir.config_parameter"].get_param(
            "secret_key", default=None)
        logout_url = self.env["ir.config_parameter"].get_param(
            "logout_url", default=None)
        res.update(
            url=url or False,
            secret_key=secret_key or False,
            logout_url=logout_url or False,
        )
        return res

    def set_values(self):
        super(GeneralSettings, self).set_values()
        for record in self:
            self.env['ir.config_parameter'].set_param(
                "url", record.url or '')
            self.env['ir.config_parameter'].set_param(
                'secret_key', record.secret_key or '')
            self.env['ir.config_parameter'].set_param(
                'logout_url', record.logout_url or '')
