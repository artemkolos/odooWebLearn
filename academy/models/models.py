# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Teachers(models.Model):
    _name = 'academy.teachers'

    name = fields.Char()
    biography = fields.Html()
    # course_ids = fields.One2many('academy.courses', inverse_name ='teacher_id', string="Courses")
    course_ids = fields.One2many('product.template', inverse_name='teacher_id', string="Courses")

class Courses(models.Model):
    # _name = 'academy.courses'
    _inherit = 'product.template'

    # name = fields.Char()
    teacher_id = fields.Many2one('academy.teachers', inverse_name='course_ids', string="Teacher")

    # taxes_id = fields.Many2many(relation='courses_taxes_rel')
    # supplier_taxes_id = fields.Many2many(relation='course_supplier_taxes_rel')
    # route_ids = fields.Many2many(relation='course_route_res')
    # alternative_product_ids = fields.Many2many(relation='course_alternative_product_rel')
    # accessory_product_ids = fields.Many2many(relation='course_accessory_product_rel')



