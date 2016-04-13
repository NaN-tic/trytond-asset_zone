#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.
from trytond.model import fields, ModelSQL, ModelView
from trytond.pool import PoolMeta

__all__ = ['Zone', 'Employee', 'Asset']


class Zone(ModelSQL, ModelView):
    'Zone'
    __name__ = 'asset.zone'
    __metaclass__ = PoolMeta
    name = fields.Char('Name')
    employee = fields.Many2One('company.employee', 'Employee')


class Employee:
    __name__ = 'company.employee'
    __metaclass__ = PoolMeta
    zones = fields.One2Many('asset.zone', 'employee', 'Zones', add_remove=[
            ('employee', '=', None),
            ])


class Asset:
    __name__ = 'asset'
    __metaclass__ = PoolMeta
    zone = fields.Many2One('asset.zone', 'Zone')
