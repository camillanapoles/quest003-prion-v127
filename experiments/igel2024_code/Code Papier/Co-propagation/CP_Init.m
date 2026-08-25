function S = CP_Init(file)
%% Unload variables from file and initialize
[t_lim,L,div,N_neur,tpr,uprr,uprt,uprd,s,D] = readvars(file,'Range','A1:J2');
[Kt,Kc,Kr] = readvars(file,'Range','K1:M5');

t = 0;
f = 0;
[X,Y] = meshgrid(1:div);

% Neuron matrix: [position mesh number ; upr(-1) ; upr]
NEUR = zeros(N_neur,3);
% For each neuron, the mesh elements in templating and upr zones
N2M = cell(N_neur,2);
% Particle matrix: for each mesh, the number of each assembly in it
PART = zeros(div^2,s+1,2);
% Alpha matrix: for each mesh, propensity of each reaction
ALPHA = zeros(div^2,5*s+5,2);
% Reaction Matrix: used to update the alpha matrix
K(1,:,1) = 4*D./([1:s 1]*L^2);                K(1,:,2) = 4*D./([1:s 1]*L^2);
K(2,:,1) = [Kt(2)*ones(1,s-1) 0 Kt(1)];       K(2,:,2) = [Kt(4)*ones(1,s-1) 0 Kt(3)];
K(3,:,1) = [Kr(1) Kr(2)*ones(1,s-1) 0];       K(3,:,2) = [Kr(3) Kr(4)*ones(1,s-1) 0];
K(4,:,1) = [0 Kc(1)*ones(1,s-1) 0];           K(4,:,2) = [0 Kc(3)*ones(1,s-1) 0];
K(5,:,1) = [Kc(2)*ones(1,s-1) 0 0];           K(5,:,2) = [Kc(4)*ones(1,s-1) 0 0];
% Result structure: track evolutions time, particles, reactions, UPR
RES = struct;
RES.T = [];
RES.P = [];
RES.U = [];
% Movie structure:
MOV = struct;
MOV.P = [];
MOV.N = [];

%% Neurons
% Square mesh
m = round(linspace(uprr,div+1-uprr,sqrt(N_neur)));
NEUR(:,1) = reshape((m-1)*div+m',[],1);

% Templating and UPR zones around each neuron
tp = Circle(tpr);
up = Circle(uprr);
for n=1:N_neur
    x = X(NEUR(n,1))+tp(1,:); y = Y(NEUR(n,1))+tp(2,:); m = find(x>0 & x<=div & y>0 & y<=div);
    N2M{n,1} = (x(m)-1)*div+y(m);
    
    x = X(NEUR(n,1))+up(1,:); y = Y(NEUR(n,1))+up(2,:); m = find(x>0 & x<=div & y>0 & y<=div);
    N2M{n,2} = (x(m)-1)*div+y(m);
end

%% Particles
% Initial distribution
part_n0 = repmat(round(10*s./[2:s+1 1]),1,1,2);

% Initiation at the center of the grid
updm = ones(2,1)*round(div/2) + Circle(2);
updm = (updm(1,:)-1)*div+updm(2,:);
PART(updm,:,:) = repmat(round(part_n0/length(updm)),length(updm),1);

%% Load variables into structure

S = structvar( t,t_lim,f,div,uprd,uprt,s, ...
               NEUR,N2M,K,PART,ALPHA,updm,RES,MOV );

%% Functions

function C = Circle(r)
    [a,b] = meshgrid(-r:r);
    c = find(a(:).^2+b(:).^2<r^2);
    C = [a(c) b(c)]';
end
           
end

