// This file was automatically generated from templates.soy.
// Please don't edit this file by hand.

if (typeof djProject == 'undefined') { var djProject = {}; }
if (typeof djProject.templates == 'undefined') { djProject.templates = {}; }


djProject.templates.tasksTableHeader = function(opt_data, opt_sb) {
  var output = opt_sb || new soy.StringBuilder();
  output.append('<div class="thg"><div style="" class="tc">id</div><div style="width: 40%" class="tc">description</div><div style="" class="tc">owner</div><div style="" class="tc">status</div><div style="" class="tc">est.</div><div style="" class="tc">rem.</div><div style="" class="tc"></div></div>');
  if (!opt_sb) return output.toString();
};


djProject.templates.sprintTemplate = function(opt_data, opt_sb) {
  var output = opt_sb || new soy.StringBuilder();
  output.append('<div class="sprint" data-sprint="', soy.$$escapeHtml(opt_data.sprint.id), '" data-project="', soy.$$escapeHtml(opt_data.sprint.project), '">', soy.$$escapeHtml(opt_data.sprint.name), '</div>');
  if (!opt_sb) return output.toString();
};


djProject.templates.taskTemplate = function(opt_data, opt_sb) {
  var output = opt_sb || new soy.StringBuilder();
  output.append('<div class="tc id">', soy.$$escapeHtml(opt_data.task.id), '</div><div class="tc description">', soy.$$escapeHtml(opt_data.task.description), '</div><div class="tc owner">', soy.$$escapeHtml(opt_data.task.owner ? opt_data.task.owner : '--'), '</div><div class="tc status">', soy.$$escapeHtml(opt_data.task.status), '</div><div class="tc estimated">', soy.$$escapeHtml(opt_data.task.estimated ? opt_data.task.estimated : '--'), '</div><div class="tc remaining">', soy.$$escapeHtml(opt_data.task.remaining ? opt_data.task.remaining : '--'), '</div><div id="task-more-', soy.$$escapeHtml(opt_data.task.id), '" data-id="', soy.$$escapeHtml(opt_data.task.id), '" class="tc task-more">-></div>');
  if (!opt_sb) return output.toString();
};


djProject.templates.projectTemplate = function(opt_data, opt_sb) {
  var output = opt_sb || new soy.StringBuilder();
  output.append('<div id="project-', soy.$$escapeHtml(opt_data.project.id), '">', soy.$$escapeHtml(opt_data.project.name), '</div><ul class="project-sprints" data-uri="', soy.$$escapeHtml(opt_data.project.resource_uri), '"></ul>');
  if (!opt_sb) return output.toString();
};
