# -*- coding: utf-8 -*-
from openerp import fields, models, api, _
from openerp.exceptions import except_orm

class rain_hr_payslip(models.Model):
    _inherit="hr.payslip"
    #employee_id = fields.Many2one('hr.employee','employee_id')
    hr_user_id = fields.Many2one('res.users','hr_user_id')
    @api.onchange('struct_id')
    def on_change_rain_struct_id(self):
        if self.employee_id.user_id:
            self.hr_user_id = self.employee_id.user_id
        else:
            self.hr_user_id = ""
class rain_user_department(models.Model):
    _inherit="res.users"
    department_id = fields.Many2one('hr.department','department_id')