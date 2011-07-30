$(function(){
    var oldSync = Backbone.sync;

    Backbone.sync = function(method, model, success, error){
        var newSuccess = function(resp, status, xhr){
            if(xhr.statusText === "CREATED"){
                var location = xhr.getResponseHeader('Location');
                return $.ajax({
                           url: location,
                           //success: success                           
                       });
            }
            
            return success(resp);
        };
        return oldSync(method, model, newSuccess, error);
    };
);