function out = NB_Run(S,vid)
%% Unload variables

[   t,t_lim,f,div,uprd,uprt,s, ...
    NEUR,N2M,K,PART,ALPHA,updm,RES,MOV  ]       = structvar(S);

[X,Y] = meshgrid(1:div);
N_neur = size(NEUR,1);

% UPR tracking
UPR = zeros(1,1+N_neur);

WB = waitbar(0);

clear S;

%% Body
while t<t_lim && sum(PART,'all')

    for n=1:N_neur      % Update UPR
        c = sum(PART(N2M{n,2},:),'all');
        NEUR(n,3) = max(NEUR(n,3),(c>uprd)*uprt);
        if xor(~NEUR(n,2),~NEUR(n,3))   % if neuron changes state, add elems of tpl zone to updm
            updm = [updm N2M{n,1}];
        end
    end

    if ~isempty(updm)        % eliminate duplicates
        updm = unique(updm);
    end

    for m=updm
        tp = sum(NEUR(cellfun(@(x) any(x==m),N2M(:,1)),3)==0);
        ALPHA(m,:) = updALPHA(PART(m,:),K,tp);
    end

    A = cumsum(ALPHA(:,end));
    m = find(A(end)*rand<A,1);      % find element of mesh where reaction happens
    
    [updm,P] = findreac(m,ALPHA(m,:),PART(m,:));
    PART(updm,:) = PART(updm,:)+P;

    tau = log(1/rand)/A(end);
    t = t+tau;
    
    NEUR(:,2) = NEUR(:,3);
    NEUR(:,3) = max(NEUR(:,3)-tau,0);   % Update UPR based on tau
    UPR = UPR + [NEUR(:,2)'>0 1]*tau;   % UPR tracking

    if ceil(t*1e2)~=f
        f = f+1;
        RES.T = cat(1,RES.T, t );
        RES.P = cat(1,RES.P, sum(PART) );
        RES.U = cat(1,RES.U, UPR(1:N_neur)/UPR(1+N_neur) );
        
        UPR = zeros(1,1+N_neur);
        
        waitbar(t/t_lim,WB,{append('t=',sprintf('%.2f',t)),append('t_{lim}=',sprintf('%.2f',t_lim))});
        
        if vid
            MOV.P = cat(3,MOV.P,PART);
            MOV.N = cat(3,MOV.N,NEUR(:,1:2));
        end
        
    end

end

waitbar(1,WB,'Simulation complete');

out = structvar( t,t_lim,f,div,uprd,uprt,s, ...
               NEUR,N2M,K,PART,ALPHA,updm,RES,MOV );

%% Functions

function A = updALPHA(P,K,tp)
    A1 = K(1,:).*P;
    A2 = K(2,:)*tp.*P;
    A3 = K(3,:)*P(s+1).*P;
    A4 = K(4,:).*P;
    A5 = K(5,:).*P.*([cumsum(flip(P(1:s-1)),'reverse') 0 0]-[ ones(1,floor(s/2)) zeros(1,s+1-floor(s/2))])/2;
    
    A = cumsum([A1 A2 A3 A4 A5]);
end

function [M,Q] = findreac(m,A,P)
    Q = zeros(1,s+1);
    
    a = find(A(end)*rand<A,1)-1;
    b = floor(a/(s+1));
    a = rem(a,s+1)+1;
    
    M = m;
    switch b
        case 0  %diffusion
            l = length(X);
            sd = [X(m)>1 X(m)<l Y(m)>1 Y(m)<l].*[-l l -1 1];    %check for edges of box
            r = randi(4);
            Q(a) = -1;
            if sd(r)
                Q(2,a) = 1;
                M = m+[0 sd(r)];
            end
        case 1  %templating
            if a>s
                Q(a) = 1;
            else
                Q([a a+1]) = [-1 1];
            end
        case 2  %cross-reac
            if a==1
                Q([1 s+1]) = [1 -1];
            else
                Q([a-1 a s+1]) = [1 -1 1];
            end
        case 3  %decondensation
            Q([a-1 a]) = [1 -1]; Q(1) = Q(1)+1;
        case 4  %condensation
            P(a) = P(a)-1; b = cumsum(P(1:s-a)); b = find(b(end)*rand<b,1);
            Q(a) = -1; Q(b) = Q(b)-1;
            Q(a+b) = Q(a+b)+1;
    end
end

end
