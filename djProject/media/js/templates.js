// This file was automatically generated from templates.soy.
// Please don't edit this file by hand.

if (typeof djProject == 'undefined') { var djProject = {}; }
if (typeof djProject.templates == 'undefined') { djProject.templates = {}; }


djProject.templates.tasksTableHeader = function(opt_data, opt_sb) {
  var output = opt_sb || new soy.StringBuilder();
  output.append('<div class="thg"><div style="" class="tc">id</div><div style="" class="tc">description</div><div style="" class="tc">owner</div><div style="" class="tc">status</div><div style="" class="tc">est.</div><div style="" class="tc">spend</div><div style="" class="tc">rem.</div></div>');
  if (!opt_sb) return output.toString();
};


djProject.templates.taskTemplate = function(opt_data, opt_sb) {
  var output = opt_sb || new soy.StringBuilder();
  output.append('<div class="tc id">', soy.$$escapeHtml(opt_data.task.id), '</div><div class="tc description">', soy.$$escapeHtml(opt_data.task.description), '</div><div class="tc owner">', soy.$$escapeHtml(opt_data.task.owner ? opt_data.task.owner : '--'), '</div><div class="tc status">', soy.$$escapeHtml(opt_data.task.status), '</div><div class="tc estimated">', soy.$$escapeHtml(opt_data.task.estimated ? opt_data.task.estimated : '--'), '</div><div class="tc spend">', soy.$$escapeHtml(opt_data.task.spend ? opt_data.task.spend : '--'), '</div><div class="tc remaining">', soy.$$escapeHtml(opt_data.task.remaining ? opt_data.task.remaining : '--'), '</div>');
  if (!opt_sb) return output.toString();
};


djProject.templates.projectTemplate = function(opt_data, opt_sb) {
  var output = opt_sb || new soy.StringBuilder();
  output.append('<div id="project-', soy.$$escapeHtml(opt_data.project.id), '">', soy.$$escapeHtml(opt_data.project.name), '</div>');
  if (!opt_sb) return output.toString();
};
