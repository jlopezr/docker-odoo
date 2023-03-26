from odoo import fields, models

class Keyword(models.Model):
    _name = "resources.keyword"
    _description = "Keyword filter"

    name = fields.Char(required=True, translate=True)
    parent_left = fields.Integer(index=True)
    parent_right = fields.Integer(index=True)
    color = fields.Integer()
    active = fields.Boolean(default=True)
    parent_id = fields.Many2one('resources.keyword', string='Parent Tag', ondelete='cascade', index=True)
    parent_path = fields.Char(index=True)

    _parent_store = True
    _parent_name = 'parent_id'
    _parent_order = 'name'
    _order = 'parent_left, name'

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists!"),
    ]