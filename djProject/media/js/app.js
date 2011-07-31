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
      filtered: function(project_id, sprint) {
    	  var data = {};
    	  if (project_id) {
    		  data['project'] = project_id;
    		  try {
    			  window.current_project = window.projects.get(project_id);
    		  } catch(err) { 
    			  window.current_project = null;
    		  }
    		  
    	  }
    	  if (sprint) {
    		  if (sprint == 'backlog') {
    			  data['sprint'] = 'backlog';
    			  //Save something like a mock sprint to represent backlog
    			  window.current_sprint = {attributes: {name: 'backlog', id: null}, get: function(key){this.attributes[key]}};
    	      } else {
    	    	  data['sprint'] = sprint.get('id');
    	    	  window.current_sprint = sprint; 
        	  }
    	  } else {
    		  window.current_sprint = null; 
    	  }
    	  this.url = TASK_API + "?" + $.param(data)
    	  
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
  	  		if (options && options.project) {
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

