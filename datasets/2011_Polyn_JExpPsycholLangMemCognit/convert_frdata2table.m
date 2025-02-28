load PolyEtal11_JEPLMC_data.mat

data.pres.category = data.pres_cat;
data.rec.category = data.rec_cat;

data.pres.period = zeros(size(data.pres_cat));
data.rec.period = data.rec_period;

data.pres.task = repmat(data.rec_task, 1, size(data.pres_items, 2));
data.rec.task = repmat(data.rec_task, 1, size(data.rec_items, 2));

tab = frdata2table(data, {'category', 'task', 'period'});
undef = cellfun(@(x) ~ischar(x) && isnan(x), tab.category);
tab.category(undef) = {'n/a'};

writetable(tab, '2011_Polyn.csv');
