//This file is copied to jupyter_core.jupyter_data_dir and changing it here does
//not reflect the changes there.

define(["nbextensions/widgets/widgets/js/widget", "nbextensions/widgets/widgets/js/manager", "jquery"],
  function(widget, manager, $){
    window.initialize = function(){};

    //the js library is loaded here. If the methods of the widget are invoked
    //in the browser without this being fully loaded, errors may occur
    $.getScript("https://cdn.biojs.net/msa/0.4/msa.min.gz.js", function(){
      console.log("external script loaded");
    });

    var SimpleView = widget.DOMWidgetView.extend({
      render: function(){
        //does not work for some reason
        //this.$seqOpdiv = $('<div />',{'class':"seqOp"}).text("Hello");
        //console.log(this.$seqOpdiv)
        //this.$el.append(this.$seqOpdiv);
        //this.$el.text("Hello from the other side");


        var msa = require("msa");
        var clustal = require("biojs-io-clustal");
        var m = new msa({
            el: this.$el,
        });
        clustal.read(this.model.get("value"), function(err, seqs){
          m.seqs.reset(seqs);
          m.render();
        });
      },
    });

    manager.WidgetManager.register_widget_view('SimpleView', SimpleView);
    return { "SimpleView" : SimpleView,
      load_ipython_extension: function(){
          console.log("I have been loaded ! -- my nb extension");
      }
    };
  });
