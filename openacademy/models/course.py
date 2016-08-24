# -*- coding: utf-8 -*-
from openerp import models,fields,_


class Course(models.Model):
    _name="openacademy.course"

    name = fields.Char(required=True,string="Titre")
    description = fields.Text(string="Description")
    resp_id = fields.Many2one(comodel_name="res.users",string="Responsable")
    sessions = fields.One2many(comodel_name="openacademy.session", inverse_name="course_id", string="Sessions", required=False, )

    _sql_constraints = [

        ('name_desc_check', 'CHECK name != description', 'Le titre doit être différent de la description'),
        ('name_unique', 'UNIQUE(name)', 'Le titre doit être unique'),

    ]

