// This file was automatically generated from templates.soy.
// Please don't edit this file by hand.

if (typeof djProject == 'undefined') { var djProject = {}; }
if (typeof djProject.templates == 'undefined') { djProject.templates = {}; }


djProject.templates.tasksTableHeader = function(opt_data, opt_sb) {
  var output = opt_sb || new soy.StringBuilder();
  output.append('<h2>Tasks</h2><span>', (opt_data.project) ? 'Project: ' + soy.$$escapeHtml(opt_data.project.attributes.name) : '', ' ', (opt_data.sprint) ? 'Sprint: ' + soy.$$escapeHtml(opt_data.sprint.attributes.name) : '', '</span><div id="projects-tasks-container" class="table"><div class="thg"><div style="" class="tc">id</div><div style="width: 40%" class="tc">description</div><div style="" class="tc">owner</div><div style="" class="tc">status</div><div style="" class="tc">est.</div><div style="" class="tc">rem.</div><div style="" class="tc"></div></div></div>', (opt_data.project) ? '<div id="create-task"><input id="new-task" placeholder="What needs to be done?" type="text"></div>' : '');
  if (!opt_sb) return output.toString();
};


djProject.templates.taskTemplate = function(opt_data, opt_sb) {
  var output = opt_sb || new soy.StringBuilder();
  output.append('<div class="tc id task-details"><a href="#">', soy.$$escapeHtml(opt_data.task.id), '</a></div><div class="tc description"><div class="content">', soy.$$escapeHtml(opt_data.task.description), '</div><div class="edit"><input class="description-input" type="text" value=""></div></div><div class="tc owner">', soy.$$escapeHtml(opt_data.task.owner ? opt_data.task.owner : '--'), '</div><div class="tc status">', soy.$$escapeHtml(opt_data.task.status), '</div><div class="tc estimated"><div class="content">', soy.$$escapeHtml(opt_data.task.estimated ? opt_data.task.estimated : '--'), '</div><div class="edit"><input class="estimated-input" type="text" value=""></div></div><div class="tc remaining"><div class="content">', soy.$$escapeHtml(opt_data.task.remaining ? opt_data.task.remaining : '--'), '</div><div class="edit"><input class="remaining-input" type="text" value=""></div></div><div id="task-more-', soy.$$escapeHtml(opt_data.task.id), '" data-id="', soy.$$escapeHtml(opt_data.task.id), '" class="tc task-details"><a href="#">-></a></div>');
  if (!opt_sb) return output.toString();
};


djProject.templates.sprintTemplate = function(opt_data, opt_sb) {
  var output = opt_sb || new soy.StringBuilder();
  output.append('<div class="sprint" data-sprint="', soy.$$escapeHtml(opt_data.sprint.id), '" data-project="', soy.$$escapeHtml(opt_data.sprint.project), '"><a href="#">', soy.$$escapeHtml(opt_data.sprint.name), '</a></div>');
  if (!opt_sb) return output.toString();
};


djProject.templates.projectTemplate = function(opt_data, opt_sb) {
  var output = opt_sb || new soy.StringBuilder();
  output.append('<div id="project-', soy.$$escapeHtml(opt_data.project.id), '" class="project"><a href="#">', soy.$$escapeHtml(opt_data.project.name), '</a><a href="/projects/add_member/', soy.$$escapeHtml(opt_data.project.id), '">add member</a></div><ul class="project-sprints" data-uri="', soy.$$escapeHtml(opt_data.project.resource_uri), '"><div class="backlog"><a href="#">backlog</a></ul>');
  if (!opt_sb) return output.toString();
};


djProject.templates.taskDetailsTemplate = function(opt_data, opt_sb) {
  var output = opt_sb || new soy.StringBuilder();
  output.append('<h2>Task Details</h2><ul id="task_details"><li>Id: ', soy.$$escapeHtml(opt_data.task.id), '</li><li>Owner: ', soy.$$escapeHtml(opt_data.task.owner ? opt_data.task.owner : '--'), '</li><li>Status: ', soy.$$escapeHtml(opt_data.task.status), '</li><li>Estimated: ', soy.$$escapeHtml(opt_data.task.estimated ? opt_data.task.estimated : '--'), '</li><li>Spend: ', soy.$$escapeHtml(opt_data.task.spend ? opt_data.task.spend : '--'), '</li><li>Remaining: ', soy.$$escapeHtml(opt_data.task.remaining ? opt_data.task.remaining : '--'), '</li><li>Priority: ', soy.$$escapeHtml(opt_data.task.priority ? opt_data.task.priority : '--'), '</li></ul><h2>Description</h2><p class="description">', soy.$$escapeHtml(opt_data.task.description), '</p><h2>Comments</h2><ul id="comments-list">no comments</ul><div id="create-comment"><input id="new-comment" placeholder="Something to say?" type="text"></div>');
  if (!opt_sb) return output.toString();
};


djProject.templates.commentTemplate = function(opt_data, opt_sb) {
  var output = opt_sb || new soy.StringBuilder();
  output.append('<p class="comment">', soy.$$escapeHtml(opt_data.comment.comment), '</p><span class="username">by ', soy.$$escapeHtml(opt_data.comment.username), '</span>');
  if (!opt_sb) return output.toString();
};
