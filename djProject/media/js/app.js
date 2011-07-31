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
      },
      
    });

    window.Tasks = Backbone.Collection.extend({
      url: TASK_API,
      model: window.Task,
      parse: function(data){
          return data.objects;
      },
      filtered: function(project_id, sprint_id) {
    	  if (project_id) {
    		  url = TASK_API + "?project=" + project_id;
        	  if (sprint_id) { 
        		  url = "&sprint=" + sprint_id;
        	  }
        	  this.url = url;
    	  } else {
    		  this.url = TASK_API;
    	  }
          return this.fetch();
      },
    });

    window.Sprint = Backbone.Model.extend({
        url: function(){
           return this.get('resource_uri') || this.collection.url;
        }
    });

    window.Sprints = Backbone.Collection.extend({
        url: SPRINT_API,
  	  	model: window.Sprint,
  	  	project: null,
  	  	
  	  	initialize: function(options) {
  	  		if (options.project) {
  	  			this.url = SPRINT_API + "?project=" + options.project.get('id');
  	  		}
  	  	},
        parse: function(data) {
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
	  model: window.Project,
      parse: function(data){
          return data.objects;
      }
    });
});

