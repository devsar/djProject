$(function(){

    window.TaskView = Backbone.View.extend({
      tagName: 'li',
      className: 'task',

      initialize: function() {
	      this.model.bind('change', this.render, this);
	      this.model.view = this;
	  },

      render: function(){
          $(this.el).html(djProject.templates.taskTemplate({task: this.model.toJSON()}));
          return this;
      }
    });
    
    window.ProjectView = Backbone.View.extend({
      tagName: 'li',
      className: 'project',

	initialize: function() {
      this.model.bind('change', this.render, this);
      this.model.view = this;
    },

      render: function() {
          $(this.el).html(djProject.templates.projectTemplate(this.model.toJSON()));
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
          
          window.projects = new window.Project();
          window.projects.bind('refresh', this.addProjects, this);          
          window.projects.bind('all', this.render, this);
          window.projects.fetch();
          
      },
      
      addTasks: function(){
          window.tasks.each(window.app.addTask);
      },

      addTask: function(task){      	
          var view = new TaskView({model: task});
          this.$('#projects-tasks-container').prepend(view.render().el);
      },
      
      addProjects: function(){
          window.projects.each(window.app.addProject);
      },

      addProject: function(project){      	
          var view = new ProjectView({model: project});
          this.$('#projects-container').prepend(view.render().el);
      },

    });
      
    window.app = new App();
});