# -*- coding: utf-8 -*-
##############################################################################
#    
# Copyright (C) 2016 Andrea Cometa (Apulia Software)
# Email: a.cometa@apuliasoftware.it
# Web site: http://www.apuliasoftware.it
# Copyright (C) 2012 Agile Business Group sagl (<http://www.agilebg.com>)
# Copyright (C) 2012 Domsense srl (<http://www.domsense.com>)
# Copyright (C) 2012 Associazione Odoo Italia
# (<http://www.odoo-italia.org>).
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
#
##############################################################################

from openerp.osv import fields, orm

class riba_configurazione(models.Model):

    _name = "riba.configurazione"
    _description = "Parametri di configurazione per le Ricevute Bancarie"

    _columns = {
        'name' : fields.char("Descrizione", size=64, required=True),
        'tipo' : fields.selection((('sbf', 'Salvo buon fine'),('incasso', 'Al dopo incasso')), 
            "Modalità Emissione", required=True),
        'bank_id' : fields.many2one('res.partner.bank', "Banca",
            required=True, help="Bank account used for Ri.Ba. issuing"),
            
        'acceptance_journal_id' : fields.many2one('account.journal', "Acceptance journal", 
            domain=[('type', '=', 'bank')],
            help="Journal used when Ri.Ba. is accepted by the bank"),
        'acceptance_account_id' : fields.many2one('account.account', "Acceptance account", 
            domain=[('type', '=', 'receivable')], help='Account used when Ri.Ba. is accepted by the bank'),
            
        'company_id': fields.many2one('res.company', 'Company',required=True),
        
        'accreditation_journal_id' : fields.many2one('account.journal', "Accreditation journal", 
            domain=[('type', '=', 'bank')],
            help="Journal used when Ri.Ba. amount is accredited by the bank"),
        'accreditation_account_id' : fields.many2one('account.account', "Ri.Ba. bank account", help='Account used when Ri.Ba. is accepted by the bank'),
        'bank_account_id' : fields.many2one('account.account', "Bank account", 
            domain=[('type', '=', 'liquidity')]),
        'bank_expense_account_id' : fields.many2one('account.account', "Bank Expenses account"),
        
        'unsolved_journal_id' : fields.many2one('account.journal', "Unsolved journal", 
            domain=[('type', '=', 'bank')],
            help="Journal used when Ri.Ba. is unsolved"),
        'overdue_effects_account_id' : fields.many2one('account.account', "Overdue Effects account", 
            domain=[('type', '=', 'receivable')]),
        'protest_charge_account_id' : fields.many2one('account.account', "Protest charge account"),
    }

    _defaults = {
        'company_id': lambda self,cr,uid,c: self.pool.get('res.company')._company_default_get(cr, uid, 'riba.configurazione', context=c),
    }
    
    def get_default_value_by_distinta(self, cr, uid, field_name, context=None):
        if context is None:
            context = {}
        if not context.get('active_id', False):
            return False
        distinta_pool = self.pool.get('riba.distinta')
        distinta = distinta_pool.browse(cr, uid, context['active_id'], context=context)
        return distinta.config[field_name] and distinta.config[field_name].id or False
    
    def get_default_value_by_distinta_line(self, cr, uid, field_name, context=None):
        if context is None:
            context = {}
        if not context.get('active_id', False):
            return False
        distinta_line = self.pool.get('riba.distinta.line').browse(cr, uid, context['active_id'], context=context)
        return distinta_line.distinta_id.config[field_name] and distinta_line.distinta_id.config[field_name].id or False


