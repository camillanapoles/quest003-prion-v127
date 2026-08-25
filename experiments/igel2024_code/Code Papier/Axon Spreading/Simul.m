function Simul(file,vid)

start = AS_Init(strcat(file,'.csv'));

out = AS_Run(start,vid);

if vid
    gifmaker(file,out);
    out = rmfield(out,out.MOV);
end

save(strcat(file,'.mat'),'out','-v7.3');

%% Figures
s = out.s; t_lim = out.t_lim;
T = out.RES.T; P = out.RES.P; U = out.RES.U;
N1 = sum(out.NEUR(:,2)==1); N2 = sum(out.NEUR(:,2)==2); UPR1 = U(:,1:N1)*ones(N1,1)/N1; UPR2 = U(:,N1+(1:N2))*ones(N2,1)/N2;
A = P(:,s+1); SiBi = P*[1:s 0]'; Size = P*[1:s 1]'./sum(P,2);

figure; tiledlayout(2,2);
nexttile; plot(T,A); xlim([0 t_lim]); xlabel('Time'); ylabel('A');
nexttile; plot(T,SiBi); xlim([0 t_lim]); xlabel('Time'); ylabel('\Sigma i B_i');
nexttile; plot(T,Size); xlim([0 t_lim]); xlabel('Time'); ylabel('<Size>');
nexttile; hold on; plot(T,UPR1); plot(T,UPR2); xlim([0 t_lim]); ylim([0 1]); xlabel('Time'); ylabel('% of activated UPR'); legend('Cluster 1','Cluster 2');

end