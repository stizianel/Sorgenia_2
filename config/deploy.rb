server "192.168.0.177", :app, :db, primary: true

set :application, "Sorgenia_2"
set :user, "sap_user"
set :deploy_to, "/home/#{user}/test/#{application}"
set :scm, :subversion
set :repository, "https://sorgenia-repos.e-utile.it/sorgenia/Sorgenia_2"
set :scm_username, "stizianel"
set :scm_password, "svntizi.01"
set :deploy_via, :copy
set :use_sudo, false

default_run_options[:pty] = true
ssh_options[:forward_agent] = true

after "deploy", "deploy:cleanup" # keep only the last 5 releases
after "deploy:create_symlink" do
run "chmod 777 #{latest_release}/src/*.py"
run "cp /home/sap_user/scripts/config.sav /home/sap_user/test/Sorgenia_2/current/src/config.ini"
end

