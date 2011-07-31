// This file was automatically generated from templates.soy.
// Please don't edit this file by hand.

if (typeof djProject == 'undefined') { var djProject = {}; }
if (typeof djProject.templates == 'undefined') { djProject.templates = {}; }


djProject.templates.taskTemplate = function(opt_data, opt_sb) {
  var output = opt_sb || new soy.StringBuilder();
  output.append('<div class="task', (opt_data.has_parent) ? ' child' : '', '"><div class="description">', soy.$$escapeHtml(opt_data.description), '</div><div class="owner">', soy.$$escapeHtml(opt_data.owner), '</div><div class="description">', soy.$$escapeHtml(opt_data.description), '</div><div class="status">', soy.$$escapeHtml(opt_data.status), '</div><div class="estimated"><input type="text" name="estimated" value="', soy.$$escapeHtml(opt_data.estimated), '"/></div><div class="spend"><input type="text" name="spend" value="', soy.$$escapeHtml(opt_data.spend), '"/></div><div class="remaining">', soy.$$escapeHtml(opt_data.remaining), '</div><div class="priority">', soy.$$escapeHtml(opt_data.priority), '</div></div>');
  if (!opt_sb) return output.toString();
};


djProject.templates.projectTemplate = function(opt_data, opt_sb) {
  var output = opt_sb || new soy.StringBuilder();
  output.append('<div>', soy.$$escapeHtml(opt_data.name), '</div>');
  if (!opt_sb) return output.toString();
};
