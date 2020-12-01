ax0.set_title('４つの業種の週給（週給は月平均）', fontsize=16)
handles0, labels0 = ax0.get_legend_handles_labels()
ggz=ax0.legend(handles=handles0[1:], labels=labels0[1:], loc='upper left', fancybox=True, framealpha=0.35)
for jlg in ggz.legendHandles:
    jlg.set_linewidth(3);
plt.setp(ax0.get_legend().get_texts(), fontsize=14)