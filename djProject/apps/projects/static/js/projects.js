$(function(){

    window.TaskView = Backbone.View.extend({
      tagName: 'li',
      className: 'task',

      render: function(){
          $(this.el).html(djProject.taskTemplate(this.model.toJSON()));
          return this;
      }                                        
    });
    
    window.ProjectView = Backbone.View.extend({
      tagName: 'li',
      className: 'project',

      render: function() {
          $(this.el).html(djProject.projectTemplate(this.model.toJSON()));
          return this;
      }
    });

    window.App = Backbone.View.extend({
      el: $('#main'),

      initialize: function() {
          _.bindAll(this, 'render');
          this.tasks = new window.Tasks();
          this.tasks.fetch();
          this.projects = new window.Project();
          this.projects.fetch();
      }

    });
      
    window.app = new App();
});