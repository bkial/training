# -*- coding: utf-8 -*-
from openerp import models,fields,api,exceptions,_
from datetime import timedelta
from dateutil import parser



class Session(models.Model):
    _name="openacademy.session"

    name = fields.Char(string="Nom",required=True)
    date_debut = fields.Date(string="Date début")
    duree = fields.Integer(string="Durée")
    nbr_place = fields.Integer(string="Nombre de place")
    course_id = fields.Many2one(comodel_name="openacademy.course", string="Course")
    instructeur_id=fields.Many2one(comodel_name="res.partner", string="Instructeur",
                                   domain=['|',('instructor','=',True),('category_id.name','in',('Teacher Level 1','Teacher Level 2'))])
    participants = fields.Many2many(comodel_name="res.partner", relation="session_part_rel", column1="session_id",
                                    column2="part_id", string="Particpants")
    place_occup=fields.Float(compute="fct_pourcentage_place_occup",string="Places occupées",store=True)
    date_fin = fields.Date(string="Date fin", store=True,compute='_get_end_date')
    color = fields.Integer(string="Color", required=False, )
    state = fields.Selection(string="Etat", selection=[('draft', 'Brouillon'), ('confirmed', 'Confirmée'), ('done', 'Terminée') ], required=False, default='draft' )



    @api.one
    @api.depends('nbr_place', 'participants')
    def fct_pourcentage_place_occup(self):
        if self.nbr_place > 0:
            self.place_occup = 100 * len(self.participants) / self.nbr_place
        else:
            self.place_occup = 0

    @api.onchange('nbr_place', 'participants')
    def _verify_valid_seats(self):
        if self.nbr_place < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.nbr_place < len(self.participants):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }

    @api.one
    @api.constrains('instructeur_id', 'participants')
    def _check_instructor_in_participants(self):
        if self.instructeur_id and self.instructeur_id in self.participants:
            raise exceptions.ValidationError("L'instructeur ne peut pas figurer parmis la liste des participants")



    @api.one
    @api.depends('date_debut','duree')
    def _get_end_date(self):
        if self.date_debut and self.duree:
            if self.duree <= 0:
                self.date_fin = self.date_debut
            else:
                self.date_fin = parser.parse(self.date_debut) + timedelta(days=int(self.duree))

    @api.one
    def action_draft(self):
        self.state = 'draft'

    @api.one
    def action_confirmed(self):
        self.state = 'confirmed'

    @api.one
    def action_done(self):
        self.state = 'done'
