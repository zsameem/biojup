//This file is copied to jupyter_core.jupyter_data_dir and changing it here does
//not reflect the changes there. so a symlink is created for dev purposes.

define(["nbextensions/widgets/widgets/js/widget", "nbextensions/widgets/widgets/js/manager", "jquery"],
  function(widget, manager, $){
    window.initialize = function(){};

    //the js library is loaded here. If the methods of the widget are invoked
    //in the browser without this being fully loaded, errors may occur
    $.getScript("https://cdn.biojs.net/msa/0.4/msa.min.gz.js", function(){
      console.log("external script loaded");
    });
    /*
      View for parsing a url
    */
    var MsaParseUrlView = widget.DOMWidgetView.extend({
      render: function(){
        var clustal = require("biojs-io-clustal");
        var m = new msa({
          el:this.$el.append("<div>", {id:"seqDiv"}),
        });
        clustal.read(this.model.get("parse_url"), function(err, seqs){
          m.seqs.reset(seqs);
          m.render();
        });
      },
    });
    /*
      View for MsaParseClustal widget. Parses a local clustal file and displays
      it using msa.
    */
    var MsaParseClustalView = widget.DOMWidgetView.extend({
      render: function(){
        var seq_list = this.model.get('seq_list');
        var m = new msa({
          el:this.$el.append("<div>", {id:"seqDiv"}),
          seqs: seq_list,
        });
        m.render();
      },

    });

    manager.WidgetManager.register_widget_view('MsaParseUrlView', MsaParseUrlView);
    manager.WidgetManager.register_widget_view('MsaParseClustalView', MsaParseClustalView);
    return { "MsaParseUrlView" : MsaParseUrlView, "MsaParseClustalView" : MsaParseClustalView,
      load_ipython_extension: function(){
          console.log("I have been loaded ! -- my nb extension");
      }
    };
  });
