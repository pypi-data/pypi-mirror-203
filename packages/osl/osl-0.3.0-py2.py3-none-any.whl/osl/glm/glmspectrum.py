
import mne
from sails.stft import glm_periodogram

def glm_spectrum(raw, reg_categorical=None, reg_ztrans=None, reg_unitmax=None
                 contrasts=None, fit_intercept=True,
                 window_type='hann', nperseg=None, noverlap=None, nfft=None,
                 detrend='constant', return_onesided=True, scaling='density',
                 mode='psd', fmin=None, fmax=None):

    XX = raw.get_data()
    axis = 1

    glmspec = glm_periodogram(XX, axis=axis
                              reg_categorical=reg_categorical,
                              reg_ztrans=reg_ztrans,
                              reg_unitmax=reg_unitmax,
                              contrasts=contrasts,
                              fit_intercept=fit_intercept,
                              window_type=window_type,
                              fs=raw.info['sfreq'],
                              nperseg=nperseg,
                              noverlap=noverlap,
                              nfft=nfft,
                              detrend=detrend,
                              return_onesided=return_onesided,
                              scaling=scaling,
                              mode=mode,
                              fmin=fmin,
                              fmax=fmax)

    return glmspec





##% ---------------------------


def plot_joint_spectrum(xvect, psd, rawref, ax=None, freqs='auto', base=1,
        topo_scale='joint', lw=0.5, ylabel='Power', title='', ylim=None,
        xtick_skip=1, topo_prop=1/3):

    plot_sensor_spectrum(ax, psd, rawref, xvect, base=base, lw=0.25)
    fx = prep_scaled_freq(base, xvect)

    if freqs == 'auto':
        topo_freq_inds = signal.find_peaks(psd.mean(axis=1), distance=f.shape[0]/3)[0]
    else:
        topo_freq_inds = [np.argmin(np.abs(xvect - ff)) for ff in freqs]


    # ylims are abit complicated...
    #  yl2[1] | Topos...
    #         | Topos....
    #   yl[1] |
    #         |
    #         |
    #         | --------------
    #         |
    #         |
    #   yl[0] |
    # Remove top third of y-axis and set limits
    yl = ax.get_ylim()
    if np.all(np.sign(yl) > -1):
        # Yscale all positive
        yl2 = (yl[0], yl[1]*(1+topo_prop))
        ax.set_ylim(*yl2)
        ax.spines['left'].set_bounds(*yl)

    elif len(np.unique(np.sign(yl))) == 2:
        # Yscale crosses zero
        ymx = np.max(np.abs(yl))
        yl = (-ymx, ymx)
        yl2 = (yl[0], yl[1]*(1+topo_prop*2))
        ax.set_ylim(*yl2)
        ax.spines['left'].set_bounds(*yl)

    yt = ax.get_yticks()
    inds = yt < yl[1]
    ax.set_yticks(yt[inds])

    ax.figure.canvas.draw()
    offset = ax.yaxis.get_major_formatter().get_offset()
    ax.yaxis.offsetText.set_visible(False)
    ax.text(0, yl[1], offset, ha='right')

    topo_centres = np.linspace(0, 1, len(freqs)+2)[1:-1]
    topo_width = 0.4
    topos = []
    for idx in range(len(freqs)):
        # Create topomap axis
        topo_pos = [topo_centres[idx] - 0.2, 1-topo_prop/2, 0.4, 0.2]
        topo = ax.inset_axes(topo_pos)

        topo_idx = fx[0][topo_freq_inds[idx]]
        plt.plot((topo_idx, topo_idx), yl, color=[0.7, 0.7, 0.7])
        yy = (yl[1], yl2[1]*(1-topo_prop/2))
        xx = fx[0][-1] * topo_centres[idx]
        plt.plot((topo_idx, xx), yy, color=[0.7, 0.7, 0.7])

        dat = psd[topo_freq_inds[idx], :]
        im, cn = mne.viz.plot_topomap(dat, rawref.info, axes=topo, show=False)
        topos.append(im)

    if topo_scale == 'joint':
        vmin = np.min([t.get_clim()[0] for t in topos])
        vmax = np.max([t.get_clim()[1] for t in topos])

        for t in topos:
            t.set_clim(vmin, vmax)
    else:
        vmin = 0
        vmax = 1

    cb_pos = [0.95, 1-topo_prop/2, 0.025, topo_prop/2]
    cax =  ax.inset_axes(cb_pos)

    plt.colorbar(topos[0], cax=cax)

    ax.set_title(title)
    ax.set_ylim(*yl2)


def plot_sensor_spectrum(ax, psd, raw, xvect, sensor_proj=False,
                         xticks=None, xticklabels=None, lw=0.5,
                         sensor_cols=True, base=1, ylabel=None, xtick_skip=1):

    plot_sensor_data(ax, psd, raw, base=base, sensor_cols=sensor_cols, lw=lw,
                     xvect=xvect, xticks=xticks, xticklabels=xticklabels,
                     xtick_skip=xtick_skip)
    decorate_spectrum(ax, ylabel=ylabel)
    ax.set_ylim(psd.min())

    if sensor_proj:
        axins = ax.inset_axes([0.6, 0.6, 0.37, 0.37])
        plot_channel_layout(axins, raw)


def plot_sensor_data(ax, data, raw, xvect=None, lw=0.5,
                     xticks=None, xticklabels=None,
                     sensor_cols=True, base=1, xtick_skip=1):
    if xvect is None:
        xvect = np.arange(obs.shape[0])
    fx, xticklabels, xticks = prep_scaled_freq(base, xvect)

    if sensor_cols:
        colors, pos, outlines = get_mne_sensor_cols(raw)
    else:
        colors = None

    plot_with_cols(ax, data, fx, colors, lw=lw)
    ax.set_xlim(fx[0], fx[-1])

    if xticks is not None:
        ax.set_xticks(xticks[::xtick_skip])
    if xticklabels is not None:
        ax.set_xticklabels(xticklabels[::xtick_skip])


def prep_scaled_freq(base, freq_vect):
    """Assuming ephy freq ranges for now - around 1-40Hz"""
    fx = freq_vect**base
    if base < 1:
        nticks = int(np.floor(np.sqrt(freq_vect[-1])))
        #ftick = np.array([2**ii for ii in range(6)])
        ftick = np.array([ii**2 for ii in range(1,nticks+1)])
        ftickscaled = ftick**base
    else:
        # Stick with automatic scales
        ftick = None
        ftickscaled = None
    return fx, ftick, ftickscaled


def get_mne_sensor_cols(raw, picks=None):
    if picks is not None:
        raw.pick_types(**picks)

    chs = [raw.info['chs'][i] for i in range(len(raw.info['chs']))]
    locs3d = np.array([ch['loc'][:3] for ch in chs])
    x, y, z = locs3d.T
    colors = mne.viz.evoked._rgb(x, y, z)
    pos, outlines = mne.viz.evoked._get_pos_outlines(raw.info,
                                                     range(len(raw.info['chs'])),
                                                     sphere=None)

    return colors, pos, outlines

def plot_channel_layout(ax, raw, size=30, marker='o'):

    ax.set_adjustable('box')
    ax.set_aspect('equal')

    colors, pos, outlines = get_mne_sensor_cols(raw)
    pos_x, pos_y = pos.T
    mne.viz.evoked._prepare_topomap(pos, ax, check_nonzero=False)
    ax.scatter(pos_x, pos_y,
               color=colors, s=size * .8,
               marker=marker, zorder=1)
    mne.viz.evoked._draw_outlines(ax, outlines)
