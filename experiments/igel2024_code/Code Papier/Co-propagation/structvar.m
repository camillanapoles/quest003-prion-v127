function varargout = structvar(varargin)

    if nargin > 1
        S = struct;
        for ii = 1:nargin
            S.(inputname(ii)) = varargin{ii};
        end
        varargout{1} = S;
    else
        S = varargin{1};
        fields = fieldnames(S);
        for ii = 1:length(fields)
            varargout{ii} = S.(fields{ii});
        end
    end

end