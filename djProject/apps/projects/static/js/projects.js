$(function(){

    window.TaskView = Backbone.View.extend({
      tagName: 'div',
      className: 'task',

      initialize: function() {
	      this.model.bind('change', this.render, this);
	      this.model.view = this;
	  },

      render: function(){
    	  var task = this.model.toJSON();
    	  $(this.el).addClass('tr');
    	  $(this.el).attr("id", "task-" + task.id);
          $(this.el).html(djProject.templates.taskTemplate({task: task}));
          return this;
      }
    });

    window.SprintView = Backbone.View.extend({
        tagName: 'li',
        className: 'sprint',

	    initialize: function(options) {
	        this.model.bind('change', this.render, this);
	        this.model.view = this;
	    },
	    
	    events: {
	        "click div.sprint"   : "showSprint",
	    },
	    
	    showSprint: function() {
	    	window.tasks.filtered(null, this.model);
	    },
	    
        render: function() {
            $(this.el).html(djProject.templates.sprintTemplate({sprint: this.model.toJSON()}));
            return this;
        }
      });
    
    window.ProjectView = Backbone.View.extend({
      tagName: 'li',
      className: 'project',

      initialize: function() {
    	  this.model.bind('change', this.render, this);
    	  this.model.view = this;
    	  this.sprints = new window.Sprints({project: this.model});
    	  this.sprints.bind('refresh', this.addSprints);
    	  this.sprints.view = this;
    	  //this.model.sprint.bind('all', this.render, this);
          
      },
      
      events: {
    	  "click div.project"   : "showProject",
          "click div.backlog"   : "showBacklog",
	  },

      addSprints: function(){
    	  $(this.view.el).filter('.project-sprints').html('');
    	  this.each(this.view.addSprint);
      },

      addSprint: function(sprint){      	
          var view = new SprintView({model: sprint});
          $('ul[data-uri="'+sprint.get('project_uri')+'"]').prepend(view.render().el);
      },
      
      showProject: function() {
	    	window.tasks.filtered(this.model.get("id"));
	  },
	  
	  showBacklog: function() {
	    	window.tasks.filtered(this.model.get("id"), 'backlog');
	  },
      
      render: function() {
          $(this.el).html(djProject.templates.projectTemplate({project: this.model.toJSON()}));
          this.sprints.fetch();
          return this;
      }
    });

    window.App = Backbone.View.extend({
      el: $('#main'),

      initialize: function() {
          _.bindAll(this, 'render');
          window.tasks = new window.Tasks();
          window.tasks.bind('refresh', this.addTasks, this);          
          window.tasks.bind('all', this.render, this);          
          window.tasks.fetch();

          window.projects = new window.Projects();
          window.projects.bind('refresh', this.addProjects, this);          
          window.projects.bind('all', this.render, this);
          window.projects.fetch();
          window.current_project = null;
          window.current_sprint = null;
          
      },
      
      events: {
          //"keypress #new-todo":  "createOnEnter",
          //"keyup #new-todo":     "showTooltip",
          "click .project-link a": "projectTasks",
          "keypress #new-task":  "createOnEnter"
       },
      
      addTasks: function(){
    	  $('#projects-tasks').html(djProject.templates.tasksTableHeader({
    		  project: window.current_project,
    		  sprint: window.current_sprint
    	  }));
          window.tasks.each(window.app.addTask);
          window.app.input = $("#new-task");
      },

      addTask: function(task){      	
          var view = new TaskView({model: task});
          this.$('#projects-tasks-container').append(view.render().el);
      },
      
      addProjects: function(){
          window.projects.each(window.app.addProject);
      },

      addProject: function(project){      	
          var view = new ProjectView({model: project});
          this.$('#projects-container').prepend(view.render().el);
      },
      newAttributes: function() {
    	  
          data =  {}
          if (window.current_project) {
        	  data['project'] = window.current_project.get('resource_uri');
          }
          
          if (window.current_sprint) { 
        	  data['sprint'] = window.current_sprint.get('resource_uri');
          }
          data['description'] = window.app.input.val();
          return data;
      },
      createOnEnter: function(e){
    	  if (e.keyCode != 13) return;
          window.tasks.create(this.newAttributes());
          this.input.val('');
      }

    });
      
    window.app = new App();
});