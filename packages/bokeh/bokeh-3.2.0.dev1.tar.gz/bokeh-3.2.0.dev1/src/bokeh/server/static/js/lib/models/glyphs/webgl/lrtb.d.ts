import { ReglWrapper } from "./regl_wrap";
import { SingleMarkerGL } from "./single_marker";
import { GLMarkerType } from "./types";
import type { LRTBView } from "../lrtb";
export declare class LRTBGL extends SingleMarkerGL {
    readonly glyph: LRTBView;
    constructor(regl_wrapper: ReglWrapper, glyph: LRTBView);
    get marker_type(): GLMarkerType;
    protected _set_data(): void;
    protected _set_once(): void;
}
//# sourceMappingURL=lrtb.d.ts.map