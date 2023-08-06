import { Transform } from "./base";
import { BaseMarkerGL, MarkerVisuals } from "./base_marker";
import { ReglWrapper } from "./regl_wrap";
import { GLMarkerType } from "./types";
import { type GlyphView } from "../glyph";
export type SingleMarkerGlyphView = GlyphView & {
    visuals: MarkerVisuals;
    glglyph?: SingleMarkerGL;
};
export declare abstract class SingleMarkerGL extends BaseMarkerGL {
    readonly glyph: SingleMarkerGlyphView;
    constructor(regl_wrapper: ReglWrapper, glyph: SingleMarkerGlyphView);
    abstract get marker_type(): GLMarkerType;
    protected _get_visuals(): MarkerVisuals;
    draw(indices: number[], main_glyph: SingleMarkerGlyphView, transform: Transform): void;
    protected _draw_impl(indices: number[], transform: Transform, main_gl_glyph: SingleMarkerGL, marker_type: GLMarkerType): void;
}
//# sourceMappingURL=single_marker.d.ts.map