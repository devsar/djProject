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
  
    window.Task = Backbone.Model.extend({
      url: function(){
         return this.get('resource_uri') || this.collection.url;
      }
    });

    window.Tasks = Backbone.Collection.extend({
      url: TASK_API,

      parse: function(data){
          return data.objects;
      }
    });
    
    window.Project = Backbone.Model.extend({
      url: function(){
         return this.get('resource_uri') || this.collection.url;
      }
    });

    window.Projects = Backbone.Collection.extend({
      url: PROJECT_API,

      parse: function(data){
          return data.objects;
      }
    });
});

