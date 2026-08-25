function gifmaker(filename,out)

filename = append(filename,'.gif');

PART = out.MOV.P; NEUR = out.MOV.N;
div = out.div;
[X,Y] = meshgrid(1:div);
s = out.s;
f = out.f;

mapcol = [ autumn(s) ; 0 .9 0 ];       % A green, B red/yellow based on size

% Setup figure
figure('units','normalized','outerposition',[0 0 1 1]); hold on; axis([0 div+1 0 div+1]); view(15,45);
set(gca,'xtick',[]); set(gca,'ytick',[]); set(gca,'ztick',[]); set(gca,'Color','k');

for i=1:f
    P = PART(:,:,i); N = NEUR(:,:,i);

    % Neurons & axons in white/pink based on UPR
    for j=1:length(N)
    n(j) = scatter(X(N(j,1)),Y(N(j,1)),50,[1 N(j,2)==0 1],'+','LineWidth',3);
        if N(j,3)
            ax(j) = plot([X(N(j,1)) X(N(N(j,3),1))],[Y(N(j,1)) Y(N(N(j,3),1))],Color=[1 N(j,2)==0 1]);
        end
    end
    
    % Particles
    VIS = [];
    for j=1:s+1
        ind = repelem(1:div^2,P(:,j));
        l = length(ind);
        VIS = [ VIS ;
        [ X(ind)'+rand(l,1)-.5 Y(ind)'+rand(l,1)-.5 ((j<=s)*25+(j>s)*50)*ones(l,1) repmat(mapcol(j,:),l,1) ] ];
    end
    VIS = VIS(randperm(size(VIS,1)),:);
    p = scatter(VIS(:,1),VIS(:,2),VIS(:,3),VIS(:,4:6),'filled');

    im = frame2im(getframe);
    [A,map] = rgb2ind(im,256);
    if i == 1
        imwrite(A,map,filename,"gif","LoopCount",Inf,"DelayTime",.1);
    else
        imwrite(A,map,filename,"gif","WriteMode","append","DelayTime",.1);
    end
    
    delete(n); delete(ax); delete(p);
    
end

    close;

end