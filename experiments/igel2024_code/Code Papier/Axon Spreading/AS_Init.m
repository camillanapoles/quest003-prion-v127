function S = AS_Init(file)
%% Unload variables from file and initialize
[t_lim,L,div,s,D,init] = readvars(file,'Range','A1:F2');
[N_neur,tpr,uprr,uprt,uprd,N_ax,r_ax,Kt,Kc,Kr] = readvars(file,'Range','G1:P3');

t = 0;
f = 0;
[X,Y] = meshgrid(1:div);

% Neuron matrix: [position mesh index ; cluster ; upr(-1) ; upr ; axon]
NEUR = zeros(sum(N_neur),5);
% For each neuron, the mesh elements in templating and upr zones
N2M = cell(sum(N_neur),2);
% Particle matrix: for each mesh, the number of each assembly in it
PART = zeros(div^2,s+1);
% Alpha matrix: for each mesh, propensity of each reaction
ALPHA = zeros(div^2,5*s+5);
% Reaction Matrix: used to update the alpha matrix
K       = 4*D./([1:s 1]*L^2);           % Diffusion
K(2,:)  = [Kt(2)*ones(1,s-1) 0 Kt(1)];  % Templating
K(3,:)  = [Kr(1) Kr(2)*ones(1,s-1) 0];  % Conf change & Catal Depol
K(4,:)  = [0 Kc(1)*ones(1,s-1) 0];      % Decondensing
K(5,:)  = [Kc(2)*ones(1,s-1) 0 0];      % Condensing
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

of = 0;
for i=1:2
    Nn = N_neur(i); Na = N_ax(i);
    m = (i==2)*div - 2*(i-1.5)*(uprr(i)+(0:ceil(sqrt(Nn))));
    m = reshape((m-1)*div+m',[],1);
    NEUR(of+(1:Nn),1:2) = [m(randperm(length(m),Nn)) i*ones(Nn,1)];
    NEUR(of+(1:Na),5) = (i==1)*N_neur(1) + randi(N_neur(~(i-1)+1),Na,1);
    of = of+N_neur(i);
end

% tpl and upr zones around each neuron, check for edges

for i=1:size(NEUR,1)
    tp = Circle(tpr(NEUR(i,2)));
    x = X(NEUR(i,1))+tp(1,:); y = Y(NEUR(i,1))+tp(2,:); m = find(x>0 & x<=div & y>0 & y<=div);
    M = (x(m)-1)*div+y(m);
    if NEUR(i,5)    % if linked to another neuron, add tpl zone for axon
        M = [M Axon(NEUR([i NEUR(i,5)],1),r_ax(NEUR(i,2)))];
    end
    N2M{i,1} = M;
    
    up = Circle(uprr(NEUR(i,2)));
    x = X(NEUR(i,1))+up(1,:); y = Y(NEUR(i,1))+up(2,:); m = find(x>0 & x<=div & y>0 & y<=div);
    N2M{i,2} = (x(m)-1)*div+y(m);
end

%% Particles
% Initial distribution
part_n0 = round(10*s./[2:s+1 1]);

% Initiation at one of the clusters
XY = (init==2)*div - 2*(init-1.5)*(uprr(init)+(ceil(sqrt(N_neur(init)))-1)/2); % middle of the cluster
updm = ones(2,1)*XY + Circle(2);
updm = (updm(1,:)-1)*div+updm(2,:);
PART(updm,:) = repmat(round(part_n0/length(updm)),length(updm),1);

%% Load variables into structure

S = structvar( t,t_lim,f,div,uprd,uprt,s, ...
               NEUR,N2M,K,PART,ALPHA,updm,RES,MOV );

%% Functions

function C = Circle(r)
    [a,b] = meshgrid(-r:r);
    c = find(a(:).^2+b(:).^2<r^2);
    C = [a(c) b(c)]';
end

function M = Axon(N,r)
    N = [X(N(1)) Y(N(1));X(N(2)) Y(N(2))];
    [n,I] = max(1+abs(N(1,:)-N(2,:)));
    IJ = round([linspace(N(1,1),N(2,1),n);linspace(N(1,2),N(2,2),n)]);
    n = max(0,n-1);
    M = reshape((IJ(1,2:n+1)-1)*div+IJ(2,2:n+1)+((I>1)*div+(I<2))*(-r:r)',1,[]);
end
           
end

