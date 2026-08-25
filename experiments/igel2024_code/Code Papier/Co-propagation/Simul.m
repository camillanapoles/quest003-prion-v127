function Simul(file,vid)

start = CP_Init(strcat(file,'.csv'));

out = CP_Run(start,vid);

if vid
    gifmaker(file,out);
    out = rmfield(out,out.MOV);
end

save('CoPropagation','out','-v7.3');

%% Figures
s = out.s; t_lim = out.t_lim;
T = out.RES.T; P1 = out.RES.P(:,:,1); P2 = out.RES.P(:,:,2); U = out.RES.U; N = size(out.NEUR,1); UPR = U*ones(N,1)/N;
A1 = P1(:,s+1); SiBi1 = P1*[1:s 0]'; Size1 = P1*[1:s 1]'./sum(P1,2);
A2 = P2(:,s+1); SiBi2 = P2*[1:s 0]'; Size2 = P2*[1:s 1]'./sum(P2,2);

figure; tiledlayout(2,2);
nexttile; hold on; plot(T,A1); plot(T,A2); xlim([0 t_lim]); xlabel('Time'); ylabel('A'); legend('Strain 1','Strain 2');
nexttile; hold on; plot(T,SiBi1); plot(T,SiBi2); xlim([0 t_lim]); xlabel('Time'); ylabel('\Sigma i B_i'); legend('Strain 1','Strain 2');
nexttile; hold on; plot(T,Size1); plot(T,Size2); xlim([0 t_lim]); xlabel('Time'); ylabel('<Size>'); legend('Strain 1','Strain 2');
nexttile; plot(T,UPR); xlim([0 t_lim]); ylim([0 1]); xlabel('Time'); ylabel('% of activated UPR');

end