# -*- coding: utf-8 -*-

from openerp import models, fields, api

class wizard(models.TransientModel):
    _name = 'openacademy.wizard'

    def _get_default_sessions(self):
        print "context =",self._context
        #return self._context['active_id']
        return self.env['openacademy.session'].browse(self._context['active_ids'])


    session_ids = fields.Many2many(comodel_name="openacademy.session", string="Sessions", default=_get_default_sessions )
    attendee_ids = fields.Many2many(comodel_name="res.partner", string="Participants", )


    @api.one
    def action_add(self):
        for s in self.session_ids:
            s.participants += self.attendee_ids

wizard()

class course_wizard(models.TransientModel):
    _name = 'openacademy.course.wizard'


    resp_id = fields.Many2one(comodel_name="res.users", string="Responsable", required=True, )


    @api.one
    def action_add(self):
        course_ids = self.env['openacademy.course'].browse(self._context['active_ids'])
        for c in course_ids:
            c.resp_id = self.resp_id

course_wizard()