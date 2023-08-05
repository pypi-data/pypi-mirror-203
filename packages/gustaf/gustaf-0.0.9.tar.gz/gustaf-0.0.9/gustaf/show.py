"""gustaf/gustaf/show.py.

Everything related to show/visualization.
"""
import sys

import numpy as np

from gustaf import settings, utils
from gustaf._base import GustafBase

# @linux it raises error if vedo is imported inside the function.
try:
    import vedo
except ImportError as err:
    # overwrites the vedo module with an object which will throw an error
    # as soon as it is used the first time. This means that any non vedo
    # functionality works as before, but as soon as vedo is used a
    # comprehensive exception will be raised which is understandable in
    # contrast to the possible errors previously possible
    from gustaf.helpers.raise_if import ModuleImportRaiser

    vedo = ModuleImportRaiser("vedo", err)


# enable `gus.show()`
# taken from https://stackoverflow.com/questions/1060796/callable-modules
# will use this until this module is renamed
class _CallableShowDotPy(sys.modules[__name__].__class__):
    def __call__(self, *args, **kwargs):
        """call show()"""
        return show(*args, **kwargs)


sys.modules[__name__].__class__ = _CallableShowDotPy


def show(*gus_obj, **kwargs):
    """Shows using appropriate backend.

    Parameters
    -----------
    *gus_obj: gustaf objects

    Returns
    --------
    None
    """
    vis_b = settings.VISUALIZATION_BACKEND

    if vis_b.startswith("vedo"):
        return show_vedo(*gus_obj, **kwargs)
    elif vis_b.startswith("trimesh"):
        pass
    elif vis_b.startswith("matplotlib"):
        pass
    else:
        raise NotImplementedError


def show_vedo(
    *args,
    **kwargs,
):
    """`vedo.show` wrapper. Each args represent one section of window. In other
    words len(args) == N, where N corresponds to the parameter for vedo.show().

    Parameters
    -----------
    *args: Union[List[Union[gustaf_obj, vedo_obj]], Dict[str, Any]]]
    """
    # vedo plotter parameter
    N = len(args)
    offs = kwargs.get("offscreen", False)
    interact = kwargs.get("interactive", True)
    plt = kwargs.get("vedoplot", None)
    skip_clear = kwargs.get("skip_clear", False)
    close = kwargs.get("close", None)
    size = kwargs.get("size", "auto")
    cam = kwargs.get("cam", None)
    title = kwargs.get("title", "gustaf")
    return_show_list = kwargs.get("return_showable_list", False)

    def clear_vedo_plotter(plotter, num_renderers, skip_cl=skip_clear):
        """enough said."""
        # for whatever reason it is desired
        if skip_cl:
            return None

        for i in range(num_renderers):
            plotter.clear(at=i)

        return None

    def cam_tuple_to_list(dict_cam):
        """if entity is tuple, turns it into list."""
        if dict_cam is None:
            return None

        for key, value in dict_cam.items():
            if isinstance(value, tuple):
                dict_cam[key] = list(value)

        return dict_cam

    # get plotter
    if plt is None:
        plt = vedo.Plotter(
            N=N, sharecam=False, offscreen=offs, size=size, title=title
        )

    else:
        # check if plt has enough Ns
        trueN = np.prod(plt.shape)
        clear_vedo_plotter(plt, trueN)  # always clear.
        if trueN != N:
            utils.log.warning(
                "Number of args exceed given vedo.Plotter's capacity.",
                "Assigning a new one",
            )
            title = plt.title
            if close:  # only if it is explicitly stated
                plt.close()  # Hope that this truly releases..
            # assign a new one
            plt = vedo.Plotter(
                N=N, sharecam=False, offscreen=offs, size=size, title=title
            )

    # loop and plot
    for i, arg in enumerate(args):
        # form valid input type.
        if isinstance(arg, dict):
            show_list = list(arg.values())
        elif isinstance(arg, list):
            show_list = arg.copy()
        else:
            # raise TypeError(
            #     "For vedo_show, only list or dict is valid input")
            utils.log.debug(
                "one of args for show_vedo is neither `dict` nor",
                "`list`. Putting it naively into a list.",
            )
            show_list = [arg]

        # quick check if the list is gustaf or non-gustaf
        # if gustaf, make it vedo-showable.
        # if there's spline, we need to pop the element and
        # extend showables to the list.
        # A show_list is a list to be plotted into a single sub frame of the
        # plot
        list_of_showables = []
        for sl in show_list:
            if not isinstance(sl, list):
                sl = [sl]
            for k, item in enumerate(sl):
                if isinstance(item, GustafBase):
                    tmp_showable = item.showable(backend="vedo", **kwargs)
                    # splines return dict
                    # - maybe it is time to do some typing..
                    if isinstance(tmp_showable, dict):
                        # add to extend later
                        list_of_showables.extend(list(tmp_showable.values()))
                    else:
                        # replace gustaf_obj with vedo_obj.
                        list_of_showables.append(tmp_showable)
                else:
                    list_of_showables.extend(sl)
        # set interactive to true at last element
        if int(i + 1) == len(args):
            plt.show(
                list_of_showables,
                at=i,
                interactive=interact,
                camera=cam_tuple_to_list(cam),
                # offscreen=offs,
            )

        else:
            plt.show(
                list_of_showables,
                at=i,
                interactive=False,
                camera=cam_tuple_to_list(cam),
                # offscreen=offs,
            )

    if interact and not offs:
        # only way to ensure memory is released
        clear_vedo_plotter(plt, np.prod(plt.shape))

        if close or close is None:  # explicitly given or None.
            # It seems to leak some memory, but here it goes.
            plt.close()  # if i close it, this cannot be reused...
            plt = None

    if return_show_list:
        return (plt, list_of_showables)
    else:
        return plt


def _vedo_showable(obj, as_dict=False, **kwargs):
    """Generates a vedo obj based on `kind` attribute from given obj, as well
    as show_options.

    Parameters
    -----------
    obj: gustaf obj
    as_dict: bool
      If True, returns vedo objects in a dict. Corresponding main objects will
      be available with ["main"] key. Else, returns vedo.Assembly object,
      where all the objects are grouped together.
    **kwargs: kwargs
      Will try to overwrite applicable items.

    Returns
    --------
    vedo_obj: vedo obj
    """
    # incase kwargs are defined, we will make a copy of the object and
    # try to overwrite all the applicable kwargs.
    if kwargs:
        # keep original ones and assign new show_options temporarily
        orig_show_options = obj.show_options
        obj._show_options = obj.__show_option__(obj)
        orig_show_options.copy_valid_options(obj.show_options)
        for key, value in kwargs.items():
            try:
                obj.show_options[key] = value
            except BaseException:
                utils.log.debug(
                    f"Skipping invalid option {key} for "
                    f"{obj.show_options._helps}"
                )
                continue

    # minimal-initialization of vedo objects
    vedo_obj = obj.show_options._initialize_showable()
    # as dict?
    if as_dict:
        return_as_dict = dict()

    # set common values. Could be a perfect place to try :=, but we want to
    # support p3.6.
    c = obj.show_options.get("c", None)
    if c is not None:
        vedo_obj.c(c)

    alpha = obj.show_options.get("alpha", None)
    if alpha is not None:
        vedo_obj.alpha(alpha)

    lighting = obj.show_options.get("lighting", None)
    if lighting is not None:
        vedo_obj.lighting(lighting)

    vertex_ids = obj.show_options.get("vertex_ids", False)
    element_ids = obj.show_options.get("element_ids", False)
    # special treatment for vertex
    if obj.kind.startswith("vertex"):
        vertex_ids = vertex_ids | element_ids
        if element_ids:
            utils.log.debug(
                "`element_ids` option is True for Vertices. Overwriting it as"
                "vertex_ids."
            )
            element_ids = False
    if vertex_ids:
        # use vtk font. supposedly faster. And differs from cell id.
        vertex_ids = vedo_obj.labels("id", on="points", font="VTK")
        if not as_dict:
            vedo_obj += vertex_ids
        else:
            return_as_dict["vertex_ids"] = vertex_ids
    if element_ids:
        # should only reach here if this obj is not vertex
        element_ids = vedo.Points(obj.centers()).labels("id", on="points")
        if not as_dict:
            vedo_obj += element_ids
        else:
            return_as_dict["element_ids"] = element_ids

    # data plotting
    data_name = obj.show_options.get("data_name", None)
    vertex_data = obj.vertex_data.as_scalar(data_name, None)
    if data_name is not None and vertex_data is not None:
        # transfer data
        if obj.kind.startswith("edge"):
            vedo_obj.pointdata[data_name] = vertex_data[obj.edges].reshape(
                -1, vertex_data.shape[1]
            )
        else:
            vedo_obj.pointdata[data_name] = vertex_data

        # form cmap kwargs for init
        cmap_keys = ("vmin", "vmax")
        cmap_kwargs = obj.show_options[cmap_keys]
        # set a default cmap if needed
        cmap_kwargs["input_cmap"] = obj.show_options.get("cmap", "plasma")
        cmap_kwargs["alpha"] = obj.show_options.get("cmap_alpha", 1)
        # add data_name
        cmap_kwargs["input_array"] = data_name

        # set cmap
        vedo_obj.cmap(**cmap_kwargs)

        # at last, scalarbar
        # deprecated function name, keep it for now for backward compat
        sb_kwargs = obj.show_options.get("scalarbar", None)
        if sb_kwargs is not None and sb_kwargs is not False:
            sb_kwargs = dict() if isinstance(sb_kwargs, bool) else sb_kwargs
            vedo_obj.addScalarBar(**sb_kwargs)

    elif data_name is not None and vertex_data is None:
        utils.log.debug(
            f"No vertex_data named '{data_name}' for {obj}. Skipping"
        )

    # arrow plots - this is independent from data plotting.
    arrow_data_name = obj.show_options.get("arrow_data", None)
    # will raise if data is scalar
    arrow_data_value = obj.vertex_data.as_arrow(arrow_data_name, None, True)
    if arrow_data_name is not None and arrow_data_value is not None:
        from gustaf.create.edges import from_data

        # we are here because this data is not a scalar
        # is showable?
        if arrow_data_value.shape[1] not in (2, 3):
            raise ValueError(
                "Only 2D or 3D data can be shown.",
                f"Requested data is {arrow_data_value.shape[1]}",
            )

        as_edges = from_data(
            obj,
            arrow_data_value,
            obj.show_options.get("arrow_data_scale", None),
            data_norm=obj.vertex_data.as_scalar(arrow_data_name),
        )
        arrows = vedo.Arrows(
            as_edges.vertices[as_edges.edges],
            c=obj.show_options.get("arrow_data_color", "plasma"),
        )
        if not as_dict:
            vedo_obj += arrows
        else:
            return_as_dict["arrow_data"] = arrows

    axes_kw = obj.show_options.get("axes", None)
    # need to explicitly check if it is false
    if axes_kw is not None and axes_kw is not False:
        axes_kw = dict() if isinstance(axes_kw, bool) else axes_kw
        axes = vedo.Axes(vedo_obj, **axes_kw)
        if not as_dict:
            vedo_obj += axes
        else:
            return_as_dict["axes"] = axes

    # set back temporary show_options if needed
    if kwargs:
        obj._show_options = orig_show_options

    if not as_dict:
        return vedo_obj
    else:
        return_as_dict["main"] = vedo_obj
        return return_as_dict


def _trimesh_showable(obj):
    """"""
    pass


def _matplotlib_showable(obj):
    """"""
    pass


def make_showable(obj, backend=settings.VISUALIZATION_BACKEND, **kwargs):
    """Since gustaf does not natively support visualization, one of the
    following library is used to visualize gustaf (visualizable) objects: (1)
    vedo -> Fast, offers a lot of features (2) trimesh -> Fast, compatible with
    old OpenGL (3) matplotlib -> Slow, offers vector graphics.

    This determines showing types using `whatami`.

    Parameters
    -----------
    obj: gustaf-objects
    backend: str
      (Optional) Default is `gustaf.settings.VISUALIZATION_BACKEND`.
      Options are: "vedo" | "trimesh" | "matplotlib"

    Returns
    --------
    showable_objs: list
      List of showable objects.
    """
    if backend.startswith("vedo"):
        return _vedo_showable(obj, **kwargs)
    elif backend.startswith("trimesh"):
        return _trimesh_showable(obj, **kwargs)
    elif backend.startswith("matplotlib"):
        return _matplotlib_showable(obj, **kwargs)
    else:
        raise NotImplementedError


# possibly relocate, is this actually used?
# could not find any usage in this repo
def interpolate_vedo_dictcam(cameras, resolutions, spline_degree=1):
    """Interpolate between vedo dict cameras.

    Parameters
    ------------
    cameras: list or tuple
    resolutions: int
    spline_degree: int
      if > 1 and splinepy is available and there are more than two cameras,
      we interpolate all the entries using spline.

    Returns
    --------
    interpolated_cams: list
    """
    try:
        import splinepy

        spp = True

    except ImportError:
        spp = False

    # quick type check loop
    cam_keys = ["pos", "focalPoint", "viewup", "distance", "clippingRange"]
    for cam in cameras:
        if not isinstance(cam, dict):
            raise TypeError("Only `dict` description of vedo cam is allowed.")
        else:
            for key in cam_keys:
                if cam[key] is None:
                    raise ValueError(
                        f"One of the camera does not contain `{key}` info"
                    )

    interpolated_cams = []
    total_cams = int(resolutions) * (len(cameras) - 1)

    if spp and spline_degree > 1 and len(cameras) > 2:
        if spline_degree > len(cameras):
            raise ValueError(
                "Not enough camera to interpolate with "
                f"spline degree {spline_degree}"
            )

        ps = []
        fs = []
        vs = []
        ds = []
        cs = []
        for cam in cameras:
            ps.append(list(cam[cam_keys[0]]))
            fs.append(list(cam[cam_keys[1]]))
            vs.append(list(cam[cam_keys[2]]))
            ds.append([float(cam[cam_keys[3]])])
            cs.append(list(cam[cam_keys[4]]))

        interpolated = dict()
        for i, prop in enumerate([ps, fs, vs, ds, cs]):
            i_spline = splinepy.BSpline()
            i_spline.interpolate_curve(
                query_points=prop,
                degree=spline_degree,
                save_query=False,
            )
            interpolated[cam_keys[i]] = i_spline.sample([total_cams])

        for i in range(total_cams):
            interpolated_cams.append(
                {
                    cam_keys[0]: interpolated[cam_keys[0]][i].tolist(),
                    cam_keys[1]: interpolated[cam_keys[1]][i].tolist(),
                    cam_keys[2]: interpolated[cam_keys[2]][i].tolist(),
                    cam_keys[3]: interpolated[cam_keys[3]][i][0],  # float?
                    cam_keys[4]: interpolated[cam_keys[4]][i].tolist(),
                }
            )

    else:
        i = 0
        for start_cam, end_cam in zip(cameras[:-1], cameras[1:]):
            if i == 0:
                interpolated = [
                    np.linspace(
                        start_cam[ckeys],
                        end_cam[ckeys],
                        resolutions,
                    ).tolist()
                    for ckeys in cam_keys
                ]

            else:
                interpolated = [
                    np.linspace(
                        start_cam[ckeys],
                        end_cam[ckeys],
                        int(resolutions + 1),
                    )[1:].tolist()
                    for ckeys in cam_keys
                ]

            i += 1

            for j in range(resolutions):
                interpolated_cams.append(
                    {
                        cam_keys[0]: interpolated[0][j],
                        cam_keys[1]: interpolated[1][j],
                        cam_keys[2]: interpolated[2][j],
                        cam_keys[3]: interpolated[3][j],  # float?
                        cam_keys[4]: interpolated[4][j],
                    }
                )

    return interpolated_cams
