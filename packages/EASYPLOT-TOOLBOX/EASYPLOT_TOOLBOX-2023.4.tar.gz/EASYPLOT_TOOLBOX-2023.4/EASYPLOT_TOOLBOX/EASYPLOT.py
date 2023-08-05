import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def CONVERT_SI_TO_INCHES(WIDTH, HEIGHT):
    """ 
    This function convert figure dimensions from meters to inches.
    
    Input:
    WIDTH    |  Figure width in SI units       |         |  Float
    HEIGHT   |  Figure height in SI units      |         |  Float
    
    Output:
    WIDTH    |  Figure width in INCHES units   |         |  Float
    HEIGHT   |  Figure height in INCHES units  |         |  Float
    """
    
    # Converting dimensions
    WIDTH /= 0.0254
    HEIGHT /= 0.0254
    
    return WIDTH, HEIGHT

def SAVE_GRAPHIC(NAME, EXT, DPI):
    """ 
    This function saves graphics according to the selected extension.

    Input: 
    NAME  | Path + name figure               |         |  String
          |   NAME = 'svg'                   |         |  
          |   NAME = 'png'                   |         |
          |   NAME = 'eps'                   |         | 
          |   NAME = 'pdf'                   |         |
    EXT   | File extension                   |         |  String
    DPI   | The resolution in dots per inch  |         |  Integer
    
    Output:
    N/A
    """
    
    plt.savefig(NAME + '.' + EXT, dpi = DPI, bbox_inches = 'tight', transparent = True)

def HISTOGRAM_CHART(DATASET, PLOT_SETUP):
    """
    See documentation in: https://wmpjrufg.github.io/EASYPLOT_TOOLBOX/
    """
    
    # Setup
    NAME = PLOT_SETUP['NAME']
    W = PLOT_SETUP['WIDTH']
    H = PLOT_SETUP['HEIGHT']
    X_AXIS_LABEL = PLOT_SETUP['X AXIS LABEL']
    X_AXIS_SIZE = PLOT_SETUP['X AXIS SIZE']
    Y_AXIS_LABEL = PLOT_SETUP['Y AXIS LABEL']
    Y_AXIS_SIZE = PLOT_SETUP['Y AXIS SIZE']
    AXISES_COLOR = PLOT_SETUP['AXISES COLOR']
    LABELS_SIZE = PLOT_SETUP['LABELS SIZE']     
    LABELS_COLOR = PLOT_SETUP['LABELS COLOR']
    CHART_COLOR = PLOT_SETUP['CHART COLOR']
    BINS = int(PLOT_SETUP['BINS'])
    KDE = PLOT_SETUP['KDE']
    DPI = PLOT_SETUP['DPI']
    EXT = PLOT_SETUP['EXTENSION']
    
    # Dataset and others information
    AUX = DATASET['DATASET']
    COLUMN = DATASET['COLUMN']
    DATA = AUX[COLUMN]
    
    # Plot
    [W, H] = CONVERT_SI_TO_INCHES(W, H)
    sns.set(style = 'ticks')
    FIG, (AX_BOX, AX_HIST) = plt.subplots(2, figsize = (W, H), sharex = True, gridspec_kw = {'height_ratios': (.15, .85)})
    sns.boxplot(x=DATA, ax = AX_BOX, color = CHART_COLOR)
    sns.histplot(DATA, ax = AX_HIST, kde = KDE, color = CHART_COLOR, bins = BINS)
    AX_BOX.set(yticks = [])
    AX_BOX.set(xlabel='')
    font = {'fontname': 'DejaVu Sans',
            'color':  LABELS_COLOR,
            'weight': 'normal',
            'size': LABELS_SIZE}
    AX_HIST.set_xlabel(X_AXIS_LABEL, fontdict = font)
    AX_HIST.set_ylabel(Y_AXIS_LABEL, fontdict = font)
    AX_HIST.tick_params(axis = 'x', labelsize = X_AXIS_SIZE, colors = AXISES_COLOR)
    AX_HIST.tick_params(axis = 'y', labelsize = Y_AXIS_SIZE, colors = AXISES_COLOR)
    plt.grid()
    sns.despine(ax = AX_HIST)
    sns.despine(ax = AX_BOX, left = True)
    
    # Save figure
    SAVE_GRAPHIC(NAME, EXT, DPI)

def LINE_CHART(DATASET, PLOT_SETUP):
	"""
    OF or FIT - Line chart

    Input:  
    DATASET     | META Optimization toolbox results                        | Py dictionary
	            |  Dictionary tags                                         |
				|    'X'     = Values NEOF or Iterations                   | Py  array[M_ITER + 1 x 1]
	            |    'Y'  = Line value by iterations                       | Py  array[N_ITER + 1 x 1][M_ITER + 1 x 1]
	            |    'LEGEND'  = Name of lines for the legend              | Py  array[N_ITER + 1 x 1]
	            |    'COLORS'  = Color of the lines                        | Py  array[N_ITER + 1 x 1]
    PLOT_SETUP  | Contains specifications of each model of chart           | Py Dictionary
                |  Dictionary tags                                         |
                |    'NAME'          == Filename output file               | String 
                |    'WIDTH'         == Width figure                       | Float
                |    'HEIGHT         == Height figure                      | Float
                |    'EXTENSION'     == Extension output file              | String 
                |    'DPI'           == Dots Per Inch - Image quality      | Integer   
				|    'MARKER'        == Line marker                        | String
				|    'MARKER SIZE'   == Marker size                        | Float
				|    'LINE WIDTH'    == Line width                         | Float
				|    'LINE STYLE'    == Line style                         | String
                |    'Y AXIS LABEL'  == Y axis label name                  | String
                |    'X AXIS LABEL'  == X axis label name                  | String
				|    'LABELS COLOR'  == Labels color                       | String
				|    'LABELS SIZE'   == Labels size                        | Float
                |    'X AXIS SIZE'   == X axis size                        | Float
                |    'Y AXIS SIZE'   == Y axis size                        | Float
                |    'AXISES COLOR'  == Axis color                         | String
                |    'GRID'          == Grid in chart                      | Boolean  
				|    'Y LOG'         == Y axis logscale                    | Boolean 
				|    'X LOG'         == X axis logscale                    | Boolean 
				|    LOC LEGEND      == Legend location                    | String
				|    SIZE LEGEND     == Legend size                        | Float
    
    Output:
    The image is saved in the current directory 
	"""
	NAME = PLOT_SETUP['NAME']
	W = PLOT_SETUP['WIDTH']
	H = PLOT_SETUP['HEIGHT']
	EXT = PLOT_SETUP['EXTENSION']
	DPI = PLOT_SETUP['DPI']
	MARKER = PLOT_SETUP['MARKER']
	MARKER_SIZE = PLOT_SETUP['MARKER SIZE']
	LINE_WIDTH = PLOT_SETUP['LINE WIDTH']
	LINE_STYLE = PLOT_SETUP['LINE STYLE']
	Y_AXIS_LABEL = PLOT_SETUP['Y AXIS LABEL']
	X_AXIS_LABEL = PLOT_SETUP['X AXIS LABEL']
	LABELS_SIZE = PLOT_SETUP['LABELS SIZE']     
	LABELS_COLOR = PLOT_SETUP['LABELS COLOR']
	X_AXIS_SIZE = PLOT_SETUP['X AXIS SIZE']
	Y_AXIS_SIZE = PLOT_SETUP['Y AXIS SIZE']
	AXISES_COLOR = PLOT_SETUP['AXISES COLOR']
	GRID = PLOT_SETUP['ON GRID?']
	YLOGSCALE = PLOT_SETUP['Y LOG']
	XLOGSCALE = PLOT_SETUP['X LOG']
	LOC = PLOT_SETUP['LOC LEGEND']
	SIZE_LEGEND = PLOT_SETUP['SIZE LEGEND']
    
	X = DATASET['X']
	# The variable is a array with the data to be distributed in the graph.
	DATA_Y = DATASET['Y']
	# A list containing the name assigned to each line of the graph in the legend
	LEGENDA = DATASET['LEGEND']
	COLORS = DATASET['COLORS']
	
    # Convert units of size figure
	W, H = CONVERT_SI_TO_INCHES(W, H)
	
	# Plot
	FIG, AX= plt.subplots(1, 1, figsize = (W, H), sharex = True)
	
    # Go through each row of the array, where each row represents a line on the graph.
	for k in range(len( DATA_Y)):
		AX.plot(X, DATA_Y[k], marker = MARKER,color =COLORS[k], linestyle = LINE_STYLE, linewidth = LINE_WIDTH, markersize = MARKER_SIZE, label=LEGENDA[k])
	if YLOGSCALE:
		AX.semilogy()
	if XLOGSCALE:
		AX.semilogx()
	font = {'fontname': 'Arial',
			'color':  LABELS_COLOR,
			'weight': 'normal',
			'size': LABELS_SIZE}
	AX.set_ylabel(Y_AXIS_LABEL, fontdict = font)
	AX.set_xlabel(X_AXIS_LABEL, fontdict = font)   
	AX.tick_params(axis = 'x', labelsize = X_AXIS_SIZE, colors = AXISES_COLOR)
	AX.tick_params(axis = 'y', labelsize = Y_AXIS_SIZE, colors = AXISES_COLOR)
	if GRID == True:
		AX.grid(color = 'grey', linestyle = '-.', linewidth = 1, alpha = 0.20)
	plt.legend(loc = LOC, prop = {'size': SIZE_LEGEND})
	SAVE_GRAPHIC(NAME, EXT, DPI)

def SCATTER_PLOT(DATASET, PLOT_SETUP):    

    NAME = PLOT_SETUP['NAME']
    W = PLOT_SETUP['WIDTH']
    H = PLOT_SETUP['HEIGHT']
    EXT = PLOT_SETUP['EXTENSION']
    DPI = PLOT_SETUP['DPI']
    MARKER = PLOT_SETUP['MARKER']
    MARKER_SIZE = PLOT_SETUP['MARKER SIZE']
    Y_AXIS_LABEL = PLOT_SETUP['Y AXIS LABEL']
    X_AXIS_LABEL = PLOT_SETUP['X AXIS LABEL']
    LABELS_SIZE = PLOT_SETUP['LABELS SIZE']   
    LABELS_COLOR = PLOT_SETUP['LABELS COLOR']
    X_AXIS_SIZE = PLOT_SETUP['X AXIS SIZE']
    Y_AXIS_SIZE = PLOT_SETUP['Y AXIS SIZE']
    AXISES_COLOR = PLOT_SETUP['AXISES COLOR']
    GRID = PLOT_SETUP['ON GRID?']
    YLOGSCALE = PLOT_SETUP['Y LOG']
    XLOGSCALE = PLOT_SETUP['X LOG']
    LOC = PLOT_SETUP['LOC LEGEND']
    SIZE_LEGEND = PLOT_SETUP['SIZE LEGEND']
    SMOOTH_LINE = PLOT_SETUP['SMOOTH LINE']

    X = DATASET['X']
    
    #The variable is an array with the data to be distributed in the graph.
    DATA_Y = DATASET['Y']
    
    # A list containing the name assigned to each line of the graph in the legend.
    LEGENDA = DATASET['LEGEND']
    
    #List with colors that must be used
    COLORS = DATASET['COLORS']
    
    # Convert units of size figure
    W, H = CONVERT_SI_TO_INCHES(W, H)
    FIG, AX = plt.subplots(1, 1, figsize = (W, H), sharex = True)
    
    
    # Go through each row of the array, where each row represents a line on the graph
    for k in range(len( DATA_Y)):
        plt.scatter(X, DATA_Y[k],marker = MARKER,c =COLORS[k] ,linewidths=MARKER_SIZE,label=LEGENDA[k])
        
    plt.title(NAME)
    
    # Trend line
    if SMOOTH_LINE:
        p = np.polyfit(X, DATA_Y, 1)
        plt.plot(X, np.polyval(p, X), color='b')
    
    if YLOGSCALE:
        AX.semilogy()
    if XLOGSCALE:
        AX.semilogx()
    plt.xlabel(X_AXIS_LABEL, fontsize=X_AXIS_SIZE,color = LABELS_COLOR)
    plt.ylabel(Y_AXIS_LABEL, fontsize=Y_AXIS_SIZE,color = LABELS_COLOR)
    plt.tick_params(axis = 'x', labelsize = LABELS_SIZE, colors = AXISES_COLOR, labelrotation = 90, direction = 'out',which = 'both', length = 10)
    plt.tick_params(axis = 'y', labelsize = LABELS_SIZE, colors = AXISES_COLOR)
    if GRID == True:
        AX.grid(color = 'grey', linestyle = '-.', linewidth = 1, alpha = 0.20)
    plt.legend(loc = LOC, prop = {'size': SIZE_LEGEND})
    SAVE_GRAPHIC(NAME, EXT, DPI)
    plt.show()

def HEATMAP(DATASET,PLOT_SETUP):
    NAME = PLOT_SETUP['NAME']
    W = PLOT_SETUP['WIDTH']
    H = PLOT_SETUP['HEIGHT']
    EXT = PLOT_SETUP['EXTENSION']
    DPI = PLOT_SETUP['DPI']
    SQUARE = PLOT_SETUP['SQUARE']
    ESCADA = PLOT_SETUP['MASK']
    GRID = PLOT_SETUP['ON GRID?']
    LINE_WIDTHS = PLOT_SETUP['LINE WIDTHS']
    CMAP =  PLOT_SETUP['CMAP']
    LINE_COLOR = PLOT_SETUP['LINE COLOR']
    ANNOT =  PLOT_SETUP['ANNOT']
    ANNOT_SIZE_FONT = PLOT_SETUP['ANNOT SIZE FONT']
    ANNOT_FONT_WEIGHT = PLOT_SETUP['ANNOT FONT WEIGHT']

    W, H = CONVERT_SI_TO_INCHES(W, H)


    IRIS = DATASET['DATA']

    # Create a correlation array
    CORR = IRIS.corr()

    #Check if the graph will be in the form of a ladder
    if ESCADA:
        #Remove the repeated values and those equal to 1
        mask = np.tril(CORR)
    else:
        mask = None
    
    # Creating the ladder-shaped correlation plot
    ax = sns.heatmap(CORR,center=0,linewidths= LINE_WIDTHS,xticklabels= True,
                linecolor = LINE_COLOR ,annot=ANNOT, vmin=-1,vmax=1,
                annot_kws={'fontsize':ANNOT_SIZE_FONT,'fontweight':ANNOT_FONT_WEIGHT},cmap=CMAP, square=SQUARE,mask = mask)
    
    #Invert the values of the y-axis and the graph becomes in the ladder-shaped form
    plt.gca().invert_yaxis() 
    
    if GRID == True:
        ax.grid(color = 'grey', linestyle = '-.', linewidth = 1, alpha = 0.20)
    
    ax.tick_params(axis='y', rotation=0)
    
    SAVE_GRAPHIC(NAME, EXT, DPI)
    
    plt.show()

def BAR_GRAPH(DATASET, PLOT_SETUP):
    # Group the data by resistance class and calculate the average of EMA for each group
    
    # Plot a bar chart
    NAME = PLOT_SETUP['NAME']
    W = PLOT_SETUP['WIDTH']
    H = PLOT_SETUP['HEIGHT']
    EXT = PLOT_SETUP['EXTENSION']
    DPI = PLOT_SETUP['DPI']
    FONT = PLOT_SETUP['FONT']
    Y_AXIS_LABEL = PLOT_SETUP['Y AXIS LABEL']
    X_AXIS_LABEL = PLOT_SETUP['X AXIS LABEL']
    LABELS_SIZE = PLOT_SETUP['LABELS SIZE']   
    LABELS_COLOR = PLOT_SETUP['LABELS COLOR']
    X_AXIS_SIZE = PLOT_SETUP['X AXIS SIZE']
    Y_AXIS_SIZE = PLOT_SETUP['Y AXIS SIZE']
    AXISES_COLOR = PLOT_SETUP['AXISES COLOR']
    GRID = PLOT_SETUP['ON GRID?']
    YLOGSCALE = PLOT_SETUP['Y LOG']
    XLOGSCALE = PLOT_SETUP['X LOG']
    BAR_WIDTH = PLOT_SETUP['BAR WIDTH']
    OPACITY = PLOT_SETUP['OPACITY']
    
    X = DATASET['X']
    Y = DATASET['Y']
    COLORS = DATASET['COLORS']
   
    [W, H] = CONVERT_SI_TO_INCHES(W, H)
    fig, ax = plt.subplots(1, 1, figsize = (W, H))
    error_config = {'ecolor': '0.3'}

    for k in range(len(Y)):
        ax.bar(X[k], Y[k], BAR_WIDTH, color=COLORS[k], error_kw=error_config,alpha = OPACITY)
    
    FONT = {
            'fontname': FONT,
            'color':  LABELS_COLOR,
            'weight': 'normal',
            'size': LABELS_SIZE
        }
    
    ax.set_ylabel(Y_AXIS_LABEL, fontdict = FONT)
    ax.set_xlabel(X_AXIS_LABEL, fontdict = FONT)
    ax.tick_params(axis = 'x', labelsize = X_AXIS_SIZE, colors = AXISES_COLOR)
    ax.tick_params(axis = 'y', labelsize = Y_AXIS_SIZE, colors = AXISES_COLOR)
    if YLOGSCALE:
        ax.semilogy()
    if XLOGSCALE:
        ax.semilogx()
    if GRID == True:
        ax.grid(color = 'grey', linestyle = '-.', linewidth = 1, alpha = 0.20)
    
    plt.tight_layout()
    SAVE_GRAPHIC(NAME, EXT, DPI)
    plt.show()
