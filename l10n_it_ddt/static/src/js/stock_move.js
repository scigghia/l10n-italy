
openerp.web.ListView.List.include({

    htmlDecode: function(input){
        var e = document.createElement('div');
        e.innerHTML = input;
        return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
        },
    
    render_cell: function (record, column) {
        var res = this._super(record, column);
        if (this.dataset.model == 'stock.move') {
            console.log(this.dataset.model);
            return this.htmlDecode(res);
            }
        return res;
        },

    });

