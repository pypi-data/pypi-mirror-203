"use strict";
(self["webpackChunkjupyterlab_quarto"] = self["webpackChunkjupyterlab_quarto"] || []).push([["lib_index_js"],{

/***/ "../../node_modules/css-loader/dist/cjs.js!./style/index.css":
/*!*******************************************************************!*\
  !*** ../../node_modules/css-loader/dist/cjs.js!./style/index.css ***!
  \*******************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../../../node_modules/css-loader/dist/runtime/cssWithMappingToString.js */ "../../node_modules/css-loader/dist/runtime/cssWithMappingToString.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../../node_modules/css-loader/dist/runtime/api.js */ "../../node_modules/css-loader/dist/runtime/api.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! -!../../../node_modules/css-loader/dist/cjs.js!./base.css */ "../../node_modules/css-loader/dist/cjs.js!./style/base.css");
// Imports



var ___CSS_LOADER_EXPORT___ = _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default()((_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default()));
___CSS_LOADER_EXPORT___.i(_node_modules_css_loader_dist_cjs_js_base_css__WEBPACK_IMPORTED_MODULE_2__["default"]);
// Module
___CSS_LOADER_EXPORT___.push([module.id, "\n", "",{"version":3,"sources":[],"names":[],"mappings":"","sourceRoot":""}]);
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (___CSS_LOADER_EXPORT___);


/***/ }),

/***/ "./lib/const.js":
/*!**********************!*\
  !*** ./lib/const.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "kMarkdownItMgr": () => (/* binding */ kMarkdownItMgr),
/* harmony export */   "kPackageNamespace": () => (/* binding */ kPackageNamespace)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/*
* const.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/

// The namespace for this project
const kPackageNamespace = 'jupyterlab-quarto';
// The MarkdownIt manager token.
const kMarkdownItMgr = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token(kPackageNamespace);


/***/ }),

/***/ "./lib/hooks/codemirror.js":
/*!*********************************!*\
  !*** ./lib/hooks/codemirror.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "codeMirrorHighlight": () => (/* binding */ codeMirrorHighlight),
/* harmony export */   "codeMirrorPreloadHook": () => (/* binding */ codeMirrorPreloadHook)
/* harmony export */ });
/* harmony import */ var _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/codemirror */ "webpack/sharing/consume/default/@jupyterlab/codemirror");
/* harmony import */ var _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_0__);
/*
* hooks.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/

function codeMirrorPreloadHook() {
    // TODO: Properly deal with {r}, {{r}} style expressions
    const fenced = new RegExp(/^`{3}([^\s]+)/g);
    return {
        run: async (source) => {
            const newModes = new Map();
            let match;
            while ((match = fenced.exec(source))) {
                if (!newModes.has(match[1])) {
                    newModes.set(match[1], _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_0__.Mode.ensure(match[1]));
                }
            }
            if (newModes.size) {
                Promise.all(newModes.values()).catch(console.warn);
            }
            return source;
        }
    };
}
const codeMirrorHighlight = (str, lang) => {
    if (!lang) {
        return ''; // use external default escaping
    }
    try {
        const spec = _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_0__.Mode.findBest(lang);
        if (!spec) {
            console.warn(`No CodeMirror mode: ${lang}`);
            return '';
        }
        const el = document.createElement('div');
        try {
            _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_0__.Mode.run(str, spec.mime, el);
            return el.innerHTML;
        }
        catch (err) {
            console.warn(`Failed to highlight ${lang} code`, err);
        }
    }
    catch (err) {
        console.warn(`No CodeMirror mode: ${lang}`);
        console.warn(`Require CodeMirror mode error: ${err}`);
    }
    return '';
};


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _providers_mermaid__WEBPACK_IMPORTED_MODULE_17__ = __webpack_require__(/*! ./providers/mermaid */ "./lib/providers/mermaid.js");
/* harmony import */ var _const__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./const */ "./lib/const.js");
/* harmony import */ var _providers_footnotes__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./providers/footnotes */ "./lib/providers/footnotes.js");
/* harmony import */ var _style_index_css__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../style/index.css */ "./style/index.css");
/* harmony import */ var _manager__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./manager */ "./lib/manager.js");
/* harmony import */ var _providers_divs__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! ./providers/divs */ "./lib/providers/divs.js");
/* harmony import */ var _providers_deflist__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./providers/deflist */ "./lib/providers/deflist.js");
/* harmony import */ var _providers_gridtables__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./providers/gridtables */ "./lib/providers/gridtables.js");
/* harmony import */ var _providers_sub__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./providers/sub */ "./lib/providers/sub.js");
/* harmony import */ var _providers_sup__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./providers/sup */ "./lib/providers/sup.js");
/* harmony import */ var _providers_tasklists__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ./providers/tasklists */ "./lib/providers/tasklists.js");
/* harmony import */ var _providers_cites__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! ./providers/cites */ "./lib/providers/cites.js");
/* harmony import */ var _providers_attrs__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./providers/attrs */ "./lib/providers/attrs.js");
/* harmony import */ var _providers_callouts__WEBPACK_IMPORTED_MODULE_18__ = __webpack_require__(/*! ./providers/callouts */ "./lib/providers/callouts.js");
/* harmony import */ var _providers_decorator__WEBPACK_IMPORTED_MODULE_19__ = __webpack_require__(/*! ./providers/decorator */ "./lib/providers/decorator.js");
/* harmony import */ var _providers_yaml__WEBPACK_IMPORTED_MODULE_20__ = __webpack_require__(/*! ./providers/yaml */ "./lib/providers/yaml.js");
/* harmony import */ var _providers_math__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! ./providers/math */ "./lib/providers/math.js");
/* harmony import */ var _providers_figures__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./providers/figures */ "./lib/providers/figures.js");
/* harmony import */ var _providers_figure_divs__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! ./providers/figure-divs */ "./lib/providers/figure-divs.js");
/* harmony import */ var _providers_table_captions__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! ./providers/table-captions */ "./lib/providers/table-captions.js");
/* harmony import */ var _providers_spans__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./providers/spans */ "./lib/providers/spans.js");
/* harmony import */ var _providers_shortcodes__WEBPACK_IMPORTED_MODULE_21__ = __webpack_require__(/*! ./providers/shortcodes */ "./lib/providers/shortcodes.js");






















const plugin = {
    id: `${_const__WEBPACK_IMPORTED_MODULE_1__.kPackageNamespace}:plugin`,
    autoStart: true,
    provides: _const__WEBPACK_IMPORTED_MODULE_1__.kMarkdownItMgr,
    activate: (_app) => {
        console.log('JupyterLab extension jupyterlab-quarto is activated!');
        // Create a markdown rendering manager 
        return (0,_manager__WEBPACK_IMPORTED_MODULE_2__.markdownItManager)();
    }
};
// Markdown It Extensions which provide base Pandoc behavior
const kPandocExtensions = [
    _providers_footnotes__WEBPACK_IMPORTED_MODULE_3__.footnotes,
    _providers_spans__WEBPACK_IMPORTED_MODULE_4__.spans,
    _providers_attrs__WEBPACK_IMPORTED_MODULE_5__.attrs,
    _providers_deflist__WEBPACK_IMPORTED_MODULE_6__.deflist,
    _providers_figures__WEBPACK_IMPORTED_MODULE_7__.figures,
    _providers_gridtables__WEBPACK_IMPORTED_MODULE_8__.gridtables,
    _providers_sub__WEBPACK_IMPORTED_MODULE_9__.sub,
    _providers_sup__WEBPACK_IMPORTED_MODULE_10__.sup,
    _providers_tasklists__WEBPACK_IMPORTED_MODULE_11__.tasklists,
    _providers_divs__WEBPACK_IMPORTED_MODULE_12__.divs,
    _providers_math__WEBPACK_IMPORTED_MODULE_13__.math
];
// Markdown It Extensions which provide Quarto specific behavior
const kQuartoExtensions = [
    _providers_figure_divs__WEBPACK_IMPORTED_MODULE_14__.figureDivs,
    _providers_table_captions__WEBPACK_IMPORTED_MODULE_15__.tableCaptions,
    _providers_cites__WEBPACK_IMPORTED_MODULE_16__.cites,
    _providers_mermaid__WEBPACK_IMPORTED_MODULE_17__.mermaid,
    _providers_callouts__WEBPACK_IMPORTED_MODULE_18__.callouts,
    _providers_decorator__WEBPACK_IMPORTED_MODULE_19__.decorator,
    _providers_yaml__WEBPACK_IMPORTED_MODULE_20__.yaml,
    _providers_shortcodes__WEBPACK_IMPORTED_MODULE_21__.shortcodes
];
// The extensions that should be enabled for Jupyter
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ([plugin, ...kPandocExtensions, ...kQuartoExtensions]);


/***/ }),

/***/ "./lib/manager.js":
/*!************************!*\
  !*** ./lib/manager.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "markdownItManager": () => (/* binding */ markdownItManager)
/* harmony export */ });
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/codemirror */ "webpack/sharing/consume/default/@jupyterlab/codemirror");
/* harmony import */ var _jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var markdown_it__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! markdown-it */ "webpack/sharing/consume/default/markdown-it/markdown-it");
/* harmony import */ var markdown_it__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(markdown_it__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _widgets__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./widgets */ "./lib/widgets.js");
/* harmony import */ var _hooks_codemirror__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./hooks/codemirror */ "./lib/hooks/codemirror.js");
/*
* manager.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/





// Provides resolved MarkdownIt options using the passed in options, the plugin
// options, and default options.
const resolveOptions = (widget, options, providers) => {
    // Build options table
    let allOptions = {
        html: true,
        linkify: true,
        typographer: true,
        langPrefix: `cm-s-${_jupyterlab_codemirror__WEBPACK_IMPORTED_MODULE_1__.CodeMirrorEditor.defaultConfig.theme} language-`,
        highlight: _hooks_codemirror__WEBPACK_IMPORTED_MODULE_3__.codeMirrorHighlight
    };
    for (const plugin of providers) {
        if (plugin.options) {
            try {
                // Add options for this plugin
                allOptions = { ...allOptions, ...plugin.options(widget) };
            }
            catch (err) {
                console.warn(`Failed to get options from markdown-it plugin ${plugin.id}`, err);
            }
        }
    }
    return {
        ...allOptions,
        ...options
    };
};
function markdownItManager() {
    // The plugin providers
    const pluginProviders = new Map();
    //  The IMarkdownItManager
    const manager = {
        registerPlugin(provider) {
            pluginProviders.set(provider.id, provider);
        },
        async getRenderer(widget, options = {}) {
            var _a, _b, _c, _d;
            // Fetch the list of providers
            const providers = [...pluginProviders.values()];
            providers.sort(sortRanked);
            // Create MarkdownIt instance
            const allOptions = resolveOptions(widget, options, providers);
            let md = new (markdown_it__WEBPACK_IMPORTED_MODULE_2___default())('default', allOptions);
            // Lifecycle hooks
            const preParseHooks = [];
            const postRenderHooks = [];
            // add mode pre-loading hook if using default highlighter
            if (_hooks_codemirror__WEBPACK_IMPORTED_MODULE_3__.codeMirrorHighlight === allOptions.highlight) {
                preParseHooks.push((0,_hooks_codemirror__WEBPACK_IMPORTED_MODULE_3__.codeMirrorPreloadHook)());
            }
            // Build MarkdownIt and load lifecycle hooks
            for (const provider of providers) {
                try {
                    // Load MarkdownIt plugin
                    const [plugin, ...pluginOptions] = await provider.plugin();
                    // Build MarkdownIt instance
                    md = md.use(plugin, ...pluginOptions);
                    // Build table of lifecycle hooks
                    if (((_a = provider.hooks) === null || _a === void 0 ? void 0 : _a.preParse) !== undefined) {
                        preParseHooks.push((_b = provider.hooks) === null || _b === void 0 ? void 0 : _b.preParse);
                    }
                    if (((_c = provider.hooks) === null || _c === void 0 ? void 0 : _c.postRender) !== undefined) {
                        postRenderHooks.push((_d = provider.hooks) === null || _d === void 0 ? void 0 : _d.postRender);
                    }
                }
                catch (err) {
                    console.warn(`Failed to load/use markdown-it plugin ${provider.id}`, err);
                }
            }
            // Sort hooks by rank
            preParseHooks.sort(sortRanked);
            postRenderHooks.sort(sortRanked);
            return {
                // Parse and render Markdown
                render: (content) => {
                    return md.render(content);
                },
                // Run hooks serially
                preParse: async (content) => {
                    for (const hook of preParseHooks) {
                        content = await hook.run(content);
                    }
                    return content;
                },
                // Run hooks serially
                postRender: async (node) => {
                    for (const hook of postRenderHooks) {
                        await hook.run(node);
                    }
                }
            };
        }
    };
    // Register the Renderer
    _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0__.markdownRendererFactory.createRenderer = (options) => {
        return new _widgets__WEBPACK_IMPORTED_MODULE_4__.RenderedMarkdown(options, manager);
    };
    return manager;
}
// Sorts by rank, using 100 if no default is provided.
const kDefaultRank = 100;
const sortRanked = (left, right) => {
    var _a, _b;
    return ((_a = left.rank) !== null && _a !== void 0 ? _a : kDefaultRank) - ((_b = right.rank) !== null && _b !== void 0 ? _b : kDefaultRank);
};


/***/ }),

/***/ "./lib/plugins/callouts.js":
/*!*********************************!*\
  !*** ./lib/plugins/callouts.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "calloutPlugin": () => (/* binding */ calloutPlugin)
/* harmony export */ });
/* harmony import */ var markdown_it_lib_token__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! markdown-it/lib/token */ "../../node_modules/markdown-it/lib/token.js");
/* harmony import */ var markdown_it_lib_token__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(markdown_it_lib_token__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _utils_markdownit__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./utils/markdownit */ "./lib/plugins/utils/markdownit.js");
/* harmony import */ var _divs__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./divs */ "./lib/plugins/divs.js");



const kTokCalloutOpen = "quarto_callout_open";
const kTokCalloutClose = "quarto_callout_close";
const kTokCalloutTitleOpen = "quarto_callout_title_open";
const kTokCalloutTitleClose = "quarto_callout_title_close";
const kTokCalloutContentOpen = "quarto_callout_content_open";
const kTokCalloutContentClose = "quarto_callout_content_close";
const kCalloutPrefix = "callout-";
const kCalloutRuleName = "quarto-callouts";
const calloutPlugin = (md) => {
    // Handle pandoc-style divs
    md.core.ruler.push(kCalloutRuleName, (state) => {
        const noteStartCallout = (callout, depth) => {
            if (calloutDepth == -1) {
                calloutDepth = depth;
            }
            state.env['quarto-active-callout'] = callout;
        };
        const noteCloseCallout = () => {
            calloutDepth = -1;
            state.env['quarto-active-callout'] = undefined;
        };
        const activeCallout = () => {
            return state.env['quarto-active-callout'];
        };
        const isCloseCallout = (depth) => {
            return calloutDepth === depth;
        };
        const titleOpenTok = (title) => {
            const token = new (markdown_it_lib_token__WEBPACK_IMPORTED_MODULE_0___default())(kTokCalloutTitleOpen, "", 1);
            token.tag = "div";
            token.attrs = [["class", "callout-header"]];
            if (title) {
                token.attrs.push(["title", title]);
            }
            return token;
        };
        const titleCloseTok = () => {
            const token = new (markdown_it_lib_token__WEBPACK_IMPORTED_MODULE_0___default())(kTokCalloutTitleClose, "", -1);
            token.tag = "div";
            return token;
        };
        const contentOpenTok = () => {
            const token = new (markdown_it_lib_token__WEBPACK_IMPORTED_MODULE_0___default())(kTokCalloutContentOpen, "", 1);
            token.tag = "div";
            token.attrs = [["class", "callout-body-container callout-body"]];
            return token;
        };
        const contentCloseTok = () => {
            const token = new (markdown_it_lib_token__WEBPACK_IMPORTED_MODULE_0___default())(kTokCalloutContentClose, "", -1);
            token.tag = "div";
            return token;
        };
        const outTokens = [];
        let calloutDepth = -1;
        let divDepth = 0;
        // just started callout - process title
        // finished processing title - process content
        let calloutState = "scanning";
        for (const token of state.tokens) {
            switch (calloutState) {
                case "add-title":
                    if (token.type === "heading_open") {
                        outTokens.push(titleOpenTok());
                        calloutState = "capturing-title";
                    }
                    else {
                        const callout = activeCallout();
                        outTokens.push(titleOpenTok(callout.title));
                        outTokens.push(titleCloseTok());
                        calloutState = "add-body";
                    }
                    break;
                case "capturing-title":
                    if (token.type === "heading_close") {
                        outTokens.push(titleCloseTok());
                        calloutState = "add-body";
                    }
                    else {
                        outTokens.push(token);
                    }
                    break;
                case "add-body":
                    outTokens.push(contentOpenTok());
                    outTokens.push(token);
                    calloutState = "capturing-body";
                    break;
                case "scanning":
                default:
                    if (token.type === _divs__WEBPACK_IMPORTED_MODULE_1__.kTokDivOpen) {
                        divDepth++;
                        const callout = parseCallout(token.attrs);
                        if (callout) {
                            noteStartCallout(callout, divDepth);
                            calloutState = "add-title";
                            const openCallout = new (markdown_it_lib_token__WEBPACK_IMPORTED_MODULE_0___default())(kTokCalloutOpen, "", 1);
                            openCallout.attrs = openCallout.attrs || [];
                            openCallout.meta = callout;
                            outTokens.push(openCallout);
                        }
                        else {
                            outTokens.push(token);
                        }
                    }
                    else if (token.type === _divs__WEBPACK_IMPORTED_MODULE_1__.kTokDivClose) {
                        if (isCloseCallout(divDepth)) {
                            outTokens.push(contentCloseTok());
                            outTokens.push(new (markdown_it_lib_token__WEBPACK_IMPORTED_MODULE_0___default())(kTokCalloutClose, "", -1));
                            noteCloseCallout();
                        }
                        else {
                            outTokens.push(token);
                        }
                        divDepth--;
                    }
                    else {
                        outTokens.push(token);
                    }
                    break;
            }
        }
        state.tokens = outTokens;
        return false;
    });
    md.renderer.rules[kTokCalloutOpen] = renderStartCallout;
    md.renderer.rules[kTokCalloutClose] = renderEndCallout;
    md.renderer.rules[kTokCalloutTitleOpen] = renderStartCalloutTitle;
    md.renderer.rules[kTokCalloutTitleClose] = renderEndCalloutTitle;
};
// Render pandoc-style divs
function renderStartCallout(tokens, idx, _options, _env, self) {
    const token = tokens[idx];
    const callout = token.meta;
    // Add classes decorating as callout
    token.attrs = (0,_utils_markdownit__WEBPACK_IMPORTED_MODULE_2__.addClass)(`callout ${callout.clz}`, token.attrs);
    // Add class that reflects the style
    token.attrs = (0,_utils_markdownit__WEBPACK_IMPORTED_MODULE_2__.addClass)(appearanceClass(callout.appearance), token.attrs);
    return `<div ${self.renderAttrs(token)}>`;
}
// Render pandoc-style divs
function renderEndCallout() {
    return `</div>`;
}
function renderStartCalloutTitle(tokens, idx) {
    const token = tokens[idx];
    const title = (0,_utils_markdownit__WEBPACK_IMPORTED_MODULE_2__.readAttrValue)("title", token.attrs) || "";
    const startContent = `
<div class="callout-header">
<div class="callout-icon-container">
  <i class="callout-icon"></i>
</div>
<div class="callout-title-container">${title}
`;
    return startContent;
}
function renderEndCalloutTitle() {
    return `</div>\n</div>`;
}
const calloutAppearance = (val) => {
    if (val) {
        switch (val) {
            case "minimal":
                return "minimal";
            case "simple":
                return "simple";
            case "default":
            default:
                return "default";
        }
    }
    else {
        return "default";
    }
};
const parseCallout = (attrs) => {
    if (attrs === null) {
        return undefined;
    }
    const classAttr = attrs.find((attr) => { return attr[0] === "class"; });
    if (!classAttr) {
        return undefined;
    }
    const classes = classAttr[1].split(" ");
    const calloutClass = classes.find((clz) => {
        return clz.startsWith('callout-');
    });
    if (calloutClass) {
        const type = calloutClass.replace(kCalloutPrefix, "");
        const title = (0,_utils_markdownit__WEBPACK_IMPORTED_MODULE_2__.readAttrValue)("title", attrs) || type.slice(0, 1).toUpperCase() + type.slice(1);
        ;
        const appearance = calloutAppearance((0,_utils_markdownit__WEBPACK_IMPORTED_MODULE_2__.readAttrValue)("appearance", attrs));
        return {
            type: type || "note",
            clz: calloutClass,
            title,
            appearance
        };
    }
    else {
        return undefined;
    }
};
const appearanceClass = (appearance) => {
    const style = appearance || "default";
    return `callout-style-${style}`;
};


/***/ }),

/***/ "./lib/plugins/cites.js":
/*!******************************!*\
  !*** ./lib/plugins/cites.js ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "citationPlugin": () => (/* binding */ citationPlugin)
/* harmony export */ });
/*
* citation.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/
const kTokCite = "quarto_cite";
const citationPlugin = (md) => {
    // Very simple plugin example that surrounds @text with `code`
    md.core.ruler.push('quarto-citation', function replaceAtSymbol(state) {
        const tokens = state.tokens;
        for (const token of tokens) {
            if (token.type === 'inline' && token.children) {
                // Rebuild the child list
                const children = [];
                for (let i = 0; i < token.children.length; i++) {
                    const child = token.children[i];
                    if (child.type === 'text') {
                        const content = child.content;
                        const textToken = (text) => {
                            const newToken = new state.Token('text', '', 0);
                            newToken.content = text.join("");
                            return newToken;
                        };
                        let text = [];
                        const flushText = () => {
                            if (text.length) {
                                children.push(textToken(text));
                                text = [];
                            }
                        };
                        let cite = [];
                        const flushCite = () => {
                            var _a;
                            if (cite.length) {
                                // Determine the cite style
                                let style = cite[0] === "-" ? "suppress-author" : "in-text";
                                if (bracketCount > 0) {
                                    style = "normal";
                                }
                                // The classes
                                const clz = ["cite", style];
                                // If the cite ends in punctuation, trim that off and make that text
                                const puncText = [];
                                // Trim off ending punctuation
                                if ([":", ".", "#", "$", "%", "&", "-", "+", "?", "<", ">", "~", "/", "!"].includes(cite[cite.length - 1])) {
                                    puncText.push(cite[cite.length - 1]);
                                    cite = cite.slice(0, -1);
                                }
                                // Make a cite token
                                const newToken = new state.Token(kTokCite, '', 0);
                                newToken.content = cite.join("");
                                newToken.attrs = newToken.attrs || [];
                                (_a = newToken.attrs) === null || _a === void 0 ? void 0 : _a.push(["class", clz.join(" ")]);
                                children.push(newToken);
                                cite = [];
                                if (puncText.length > 0) {
                                    children.push(textToken(puncText));
                                }
                            }
                        };
                        let capture = "text";
                        let bracketCount = 0;
                        for (let j = 0; j < content.length; j++) {
                            const char = content.charAt(j);
                            if (char === "@") {
                                if ((text.length === 1 && text[0] === '-') ||
                                    text.length > 1 && text[text.length - 1] === "-" && text[text.length - 2] === "[") {
                                    cite.push('-');
                                    cite.push(char);
                                    text.pop();
                                    flushText();
                                    capture = 'cite';
                                }
                                else if (text[text.length - 1] === ' ') {
                                    flushText();
                                    cite.push(char);
                                    capture = 'cite';
                                }
                                else if (text[text.length - 1] === '-' && text[text.length - 2] === ' ') {
                                    text = text.slice(0, -1);
                                    flushText();
                                    cite.push('-');
                                    cite.push(char);
                                    capture = 'cite';
                                }
                                else if (text[text.length - 1] === '[' && text[text.length - 2] === ' ') {
                                    flushText();
                                    cite.push(char);
                                    capture = 'cite';
                                }
                                else if (text.length === 0) {
                                    cite.push(char);
                                    capture = 'cite';
                                }
                                else {
                                    if (capture === 'cite') {
                                        cite.push(char);
                                    }
                                    else {
                                        text.push(char);
                                    }
                                }
                            }
                            else if (char === " ") {
                                capture = 'text';
                                flushCite();
                                text.push(char);
                            }
                            else if (char === "[") {
                                bracketCount++;
                                text.push(char);
                            }
                            else if (char === "]") {
                                bracketCount--;
                                capture = 'text';
                                flushCite();
                                text.push(char);
                            }
                            else {
                                if (capture === 'cite') {
                                    cite.push(char);
                                }
                                else {
                                    text.push(char);
                                }
                            }
                        }
                        flushCite();
                        flushText();
                    }
                    else {
                        children.push(child);
                    }
                }
                token.children = children.length > 0 ? children : null;
            }
        }
    });
    md.renderer.rules[kTokCite] = renderCite;
};
// Render pandoc-style divs
function renderCite(tokens, idx, _options, _env, self) {
    const token = tokens[idx];
    const citeContent = `<code ${self.renderAttrs(token)}>${token.content}</code>`;
    return citeContent;
}


/***/ }),

/***/ "./lib/plugins/decorator.js":
/*!**********************************!*\
  !*** ./lib/plugins/decorator.js ***!
  \**********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "decoratorPlugin": () => (/* binding */ decoratorPlugin)
/* harmony export */ });
/* harmony import */ var markdown_it_lib_token__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! markdown-it/lib/token */ "../../node_modules/markdown-it/lib/token.js");
/* harmony import */ var markdown_it_lib_token__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(markdown_it_lib_token__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _utils_html__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./utils/html */ "./lib/plugins/utils/html.js");
/* harmony import */ var _divs__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./divs */ "./lib/plugins/divs.js");
/* harmony import */ var _figures__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./figures */ "./lib/plugins/figures.js");
/* harmony import */ var _utils_tok__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./utils/tok */ "./lib/plugins/utils/tok.js");
/* harmony import */ var _math__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./math */ "./lib/plugins/math.js");






const kTokDecorator = "quarto_decorator";
const kQuartoDecoratorOptions = "quarto-decorator-options";
const decoratorPlugin = (md) => {
    md.core.ruler.push('quarto-decorator', function replaceAtSymbol(state) {
        const outTokens = [];
        for (const token of state.tokens) {
            if (token.type === "fence" && !token.attrs && token.info) {
                outTokens.push(decoratorTokForToken(token));
            }
            else if (token.type === _utils_tok__WEBPACK_IMPORTED_MODULE_1__.kTokHeadingOpen && token.attrs) {
                outTokens.push(decoratorTokForToken(token));
            }
            else if (token.type === _divs__WEBPACK_IMPORTED_MODULE_2__.kTokDivOpen && token.attrs) {
                outTokens.push(decoratorTokForToken(token));
            }
            else if (token.type === _figures__WEBPACK_IMPORTED_MODULE_3__.kTokFigureOpen && token.attrs) {
                outTokens.push(decoratorTokForToken(token, { hide: { attributes: true } }));
            }
            else if (token.type === _utils_tok__WEBPACK_IMPORTED_MODULE_1__.kTokTableOpen && token.attrs) {
                outTokens.push(decoratorTokForToken(token));
            }
            else if (token.type === _math__WEBPACK_IMPORTED_MODULE_4__.kTokMathBlock && token.attrs) {
                outTokens.push(decoratorTokForToken(token));
            }
            outTokens.push(token);
        }
        state.tokens = outTokens;
    });
    md.renderer.rules[kTokDecorator] = renderDecorator;
};
function decoratorTokForToken(token, options) {
    const decoratorTok = new (markdown_it_lib_token__WEBPACK_IMPORTED_MODULE_0___default())(kTokDecorator, "div", 1);
    decoratorTok.attrs = token.attrs;
    decoratorTok.info = token.info;
    if (options) {
        decoratorTok.meta = decoratorTok.meta || {};
        decoratorTok.meta[kQuartoDecoratorOptions] = options;
    }
    return decoratorTok;
}
// Render pandoc-style divs
function renderDecorator(tokens, idx) {
    var _a;
    const token = tokens[idx];
    const decoratorOptions = (_a = token.meta) === null || _a === void 0 ? void 0 : _a[kQuartoDecoratorOptions];
    if (token.info) {
        return (0,_utils_html__WEBPACK_IMPORTED_MODULE_5__.decorator)([token.info]);
    }
    else {
        return (0,_utils_html__WEBPACK_IMPORTED_MODULE_5__.attributeDecorator)(token, decoratorOptions);
    }
}


/***/ }),

/***/ "./lib/plugins/divs.js":
/*!*****************************!*\
  !*** ./lib/plugins/divs.js ***!
  \*****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "divPlugin": () => (/* binding */ divPlugin),
/* harmony export */   "kDivRuleName": () => (/* binding */ kDivRuleName),
/* harmony export */   "kTokDivClose": () => (/* binding */ kTokDivClose),
/* harmony export */   "kTokDivOpen": () => (/* binding */ kTokDivOpen)
/* harmony export */ });
/* harmony import */ var _utils_markdownit__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./utils/markdownit */ "./lib/plugins/utils/markdownit.js");

const kDivRuleName = "pandocDiv";
const kTokDivOpen = 'pandoc_div_open';
const kTokDivClose = 'pandoc_div_close';
const divPlugin = (md) => {
    // Render pandoc-style divs
    function renderStartDiv(tokens, idx, _options, _env, self) {
        // Add a class to designate that this is a quarto dev
        const token = tokens[idx];
        token.attrs = (0,_utils_markdownit__WEBPACK_IMPORTED_MODULE_0__.addClass)("quarto-div", token.attrs);
        return `<div ${self.renderAttrs(token)}>`;
    }
    // Render pandoc-style divs
    function renderEndDiv() {
        return `</div>`;
    }
    // TODO Implement a better test during validation run
    // Handle pandoc-style divs
    md.block.ruler.before("fence", kDivRuleName, (state, start, _end, silent) => {
        // This is a validation run, can ignore
        if (silent) {
            return true;
        }
        // Get the line for parsing
        const lineStart = state.bMarks[start] + state.tShift[start];
        const lineEnd = state.eMarks[start];
        const line = state.src.slice(lineStart, lineEnd);
        // The current state of the divs (e.g. is there an open)
        // div. Data structure holds key that is the number of colons
        const divState = state.env.quartoOpenDivs || {};
        const incrementDivCount = (fence) => {
            state.env.quartoOpenDivs = state.env.quartoOpenDivs || {};
            const current = state.env.quartoOpenDivs[fence] || 0;
            state.env.quartoOpenDivs[fence] = Math.max(0, current + 1);
        };
        const decrementDivCount = (fence) => {
            state.env.quartoOpenDivs = state.env.quartoOpenDivs || {};
            const current = state.env.quartoOpenDivs[fence] || 0;
            state.env.quartoOpenDivs[fence] = Math.max(0, current - 1);
        };
        // Three or more colons followed by a an optional brace with attributes
        const divBraceRegex = /^(:::+)\s*(?:(\{[\s\S]+?\}))?$/;
        // Three or more colons followed by a string with no braces
        const divNoBraceRegex = /^(:::+)\s*(?:([^{}\s]+?))?$/;
        const matchers = [divBraceRegex, divNoBraceRegex];
        let match;
        for (const matcher of matchers) {
            match = matcher.exec(line);
            if (match) {
                break;
            }
        }
        if (match) {
            // There is a div here, is one already open?
            const divFence = match[1];
            const attr = match[2];
            // Is this open?
            let isOpenDiv = false;
            const openCount = divState[divFence];
            if (!openCount || openCount === 0) {
                // There isn't an existing open div at this level (number of colons)
                isOpenDiv = true;
            }
            else if (attr) {
                // If it has attributes it is always open
                isOpenDiv = true;
            }
            if (isOpenDiv) {
                // Add to the open count (or set it to 1)
                incrementDivCount(divFence);
                // Make an open token
                const token = state.push(kTokDivOpen, "div", 1);
                token.markup = line;
                // Allow this to be parsed for attributes by markdown-it-attr
                if (attr && attr.startsWith("{")) {
                    token.info = attr;
                }
                else if (attr) {
                    token.info = `{.${attr}}`;
                }
                token.block = true;
            }
            else {
                // Subtract from the open count (min zero)
                decrementDivCount(divFence);
                // Make a close token
                const token = state.push(kTokDivClose, "div", -1);
                token.markup = line;
            }
            state.line = start + 1;
            return true;
        }
        else {
            return false;
        }
    }, { alt: [] });
    md.renderer.rules[kTokDivOpen] = renderStartDiv;
    md.renderer.rules[kTokDivClose] = renderEndDiv;
};


/***/ }),

/***/ "./lib/plugins/figure-divs.js":
/*!************************************!*\
  !*** ./lib/plugins/figure-divs.js ***!
  \************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "figureDivsPlugin": () => (/* binding */ figureDivsPlugin)
/* harmony export */ });
/* harmony import */ var _utils_markdownit__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./utils/markdownit */ "./lib/plugins/utils/markdownit.js");
/* harmony import */ var _utils_tok__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./utils/tok */ "./lib/plugins/utils/tok.js");
/* harmony import */ var _divs__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./divs */ "./lib/plugins/divs.js");
/* harmony import */ var _figures__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./figures */ "./lib/plugins/figures.js");
/*
 * figure-divs.ts
 *
 * Copyright (C) 2020-2023 Posit Software, PBC
 *
 */




const kFigureDivRuleName = "quarto-figure-divs";
const kFigurePrefix = "fig-";
const figureDivsPlugin = (md) => {
    // Handle pandoc-style divs
    md.core.ruler.push(kFigureDivRuleName, (state) => {
        let isFigureDiv = [];
        for (let i = 0; i < state.tokens.length; i++) {
            const token = state.tokens[i];
            if (token.type === _divs__WEBPACK_IMPORTED_MODULE_0__.kTokDivOpen) {
                const id = (0,_utils_markdownit__WEBPACK_IMPORTED_MODULE_1__.readAttrValue)("id", token.attrs);
                if (id === null || id === void 0 ? void 0 : id.startsWith(kFigurePrefix)) {
                    isFigureDiv.push(true);
                    (0,_figures__WEBPACK_IMPORTED_MODULE_2__.mutateToFigureTok)(token, "open");
                }
                else {
                    // Note the div, but not a figure div
                    isFigureDiv.push(false);
                }
            }
            else if (token.type === _divs__WEBPACK_IMPORTED_MODULE_0__.kTokDivClose) {
                const isFigDiv = isFigureDiv.pop();
                if (isFigDiv) {
                    // If the preview token is paragraph, use that as the caption
                    if (i - 3 >= 0) {
                        const maybeParaStart = state.tokens[i - 3];
                        const maybeInline = state.tokens[i - 2];
                        const maybeParaEnd = state.tokens[i - 1];
                        if (maybeParaStart.type === _utils_tok__WEBPACK_IMPORTED_MODULE_3__.kTokParaOpen && maybeParaEnd.type === _utils_tok__WEBPACK_IMPORTED_MODULE_3__.kTokParaClose && maybeInline.type === _utils_tok__WEBPACK_IMPORTED_MODULE_3__.kTokInline) {
                            mutateToFigCaption(state.tokens[i - 3], "open");
                            mutateToFigCaption(state.tokens[i - 1], "close");
                        }
                    }
                    (0,_figures__WEBPACK_IMPORTED_MODULE_2__.mutateToFigureTok)(token, "close");
                }
            }
        }
    });
};
const mutateToFigCaption = (token, type) => {
    token.tag = "figcaption";
    token.type = type === "open" ? _figures__WEBPACK_IMPORTED_MODULE_2__.kTokFigCaptionClose : _figures__WEBPACK_IMPORTED_MODULE_2__.kTokFigCaptionOpen;
};


/***/ }),

/***/ "./lib/plugins/figures.js":
/*!********************************!*\
  !*** ./lib/plugins/figures.js ***!
  \********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "figuresPlugin": () => (/* binding */ figuresPlugin),
/* harmony export */   "kTokFigCaptionClose": () => (/* binding */ kTokFigCaptionClose),
/* harmony export */   "kTokFigCaptionOpen": () => (/* binding */ kTokFigCaptionOpen),
/* harmony export */   "kTokFigureClose": () => (/* binding */ kTokFigureClose),
/* harmony export */   "kTokFigureOpen": () => (/* binding */ kTokFigureOpen),
/* harmony export */   "mutateToFigureTok": () => (/* binding */ mutateToFigureTok)
/* harmony export */ });
/* harmony import */ var _utils_tok__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./utils/tok */ "./lib/plugins/utils/tok.js");
/*
 * figures.ts
 *
 * Copyright (C) 2020-2023 Posit Software, PBC
 *
 */

const kTokFigureOpen = "figure_open";
const kTokFigureClose = "figure_close";
const kTokFigCaptionOpen = "figcaption_open";
const kTokFigCaptionClose = "figcaption_close";
const mutateToFigureTok = (token, type) => {
    token.type = type === "open" ? kTokFigureOpen : kTokFigureClose;
    token.tag = "figure";
};
function figuresPlugin(md, options) {
    options = options || {};
    md.core.ruler.before("linkify", "implicit_figures", (state) => {
        // reset tabIndex on md.render()
        let tabIndex = 1;
        // do not process first and last token
        for (let i = 1, l = state.tokens.length; i < l - 1; ++i) {
            const token = state.tokens[i];
            if (token.type !== "inline") {
                continue;
            }
            // children: image alone, or link_open -> image -> link_close
            if (!token.children ||
                (token.children.length !== 1 && token.children.length !== 3)) {
                continue;
            }
            // one child, should be img
            if (token.children.length === 1 && token.children[0].type !== "image") {
                continue;
            }
            // three children, should be image enclosed in link
            if (token.children.length === 3 &&
                (token.children[0].type !== "link_open" ||
                    token.children[1].type !== "image" ||
                    token.children[2].type !== "link_close")) {
                continue;
            }
            // prev token is paragraph open
            if (i !== 0 && state.tokens[i - 1].type !== _utils_tok__WEBPACK_IMPORTED_MODULE_0__.kTokParaOpen) {
                continue;
            }
            // next token is paragraph close
            if (i !== l - 1 && state.tokens[i + 1].type !== _utils_tok__WEBPACK_IMPORTED_MODULE_0__.kTokParaClose) {
                continue;
            }
            // The image
            const image = token.children.length === 1 ? token.children[0] : token.children[1];
            // The image must have a caption to count as a figure
            if (!image.children || image.children.length === 0) {
                continue;
            }
            // We have inline token containing an image only.
            // Previous token is paragraph open.
            // Next token is paragraph close.
            // Lets replace the paragraph tokens with figure tokens.
            const figure = state.tokens[i - 1];
            mutateToFigureTok(figure, "open");
            mutateToFigureTok(state.tokens[i + 1], "close");
            if (options.dataType == true) {
                state.tokens[i - 1].attrPush(["data-type", "image"]);
            }
            if (options.link == true && token.children.length === 1) {
                token.children.unshift(new state.Token("link_open", "a", 1));
                const src = image.attrGet("src");
                if (src !== null) {
                    token.children[0].attrPush(["href", src]);
                }
                token.children.push(new state.Token("link_close", "a", -1));
            }
            if (options.figcaption == true) {
                if (image.children && image.children.length) {
                    token.children.push(new state.Token(kTokFigCaptionOpen, "figcaption", 1));
                    token.children.splice(token.children.length, 0, ...image.children);
                    token.children.push(new state.Token(kTokFigCaptionClose, "figcaption", -1));
                    image.children.length = 0;
                }
            }
            if (options.copyAttrs && image.attrs) {
                const f = options.copyAttrs === true ? "" : options.copyAttrs;
                figure.attrs = image.attrs.filter(([k]) => k.match(f));
            }
            if (options.tabindex == true) {
                // add a tabindex property
                // you could use this with css-tricks.com/expanding-images-html5
                state.tokens[i - 1].attrPush(["tabindex", String(tabIndex)]);
                tabIndex++;
            }
            if (options.lazyLoading == true) {
                image.attrPush(["loading", "lazy"]);
            }
        }
    });
}


/***/ }),

/***/ "./lib/plugins/gridtables/common/gridtables/GetCells.js":
/*!**************************************************************!*\
  !*** ./lib/plugins/gridtables/common/gridtables/GetCells.js ***!
  \**************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ getCells)
/* harmony export */ });
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Bas Verweij. All rights reserved.
 *  Licensed under the MIT License. See LICENSE in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
/**
* getCells parses the lines found for a certain row, and transforms these to
* the separate cell lines.
*
* @param lines The lines for the row.
*/
function getCells(lines) {
    const cells = [];
    for (let i = 0; i < lines[0].length; i++) {
        let cell = [];
        for (let j = 0; j < lines.length; j++) {
            const s = trimEnd(lines[j][i]);
            if ((s.length === 0) &&
                (cell.length === 0)) {
                // skip leading empty lines
                continue;
            }
            cell.push(s);
        }
        // remove trailing empty lines
        let j = cell.length - 1;
        for (; j >= 0; j--) {
            if (cell[j].length > 0) {
                break;
            }
        }
        if (j < cell.length - 1) {
            cell = cell.slice(0, j + 1);
        }
        cells.push(cell);
    }
    return cells;
}
function trimEnd(s) {
    const trimmed = s.trim();
    if (trimmed.length === 0) {
        return '';
    }
    return s.slice(0, s.indexOf(trimmed) + trimmed.length);
}


/***/ }),

/***/ "./lib/plugins/gridtables/common/gridtables/GetColumnWidths.js":
/*!*********************************************************************!*\
  !*** ./lib/plugins/gridtables/common/gridtables/GetColumnWidths.js ***!
  \*********************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ getColumnWidths)
/* harmony export */ });
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Bas Verweij. All rights reserved.
 *  Licensed under the MIT License. See LICENSE in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
/**
* getColumnWidths parses the provided line and returns the associated column widths.
*
* @param line The separator line to parse for the column widths.
* @returns The column widths for the provided line, or an empty array if the line is invalid.
*/
function getColumnWidths(line) {
    // try to parse as a row separator line
    let columnMatch = line
        .substr(1)
        .match(/[:-][-]+[:-]\+/g);
    if (columnMatch == null) {
        // try to parse as a header separator line
        columnMatch = line
            .substr(1)
            .match(/[:=][=]+[:=]\+/g);
    }
    if (columnMatch == null) {
        return [];
    }
    return columnMatch.map(s => s.length);
}


/***/ }),

/***/ "./lib/plugins/gridtables/common/markdown-it/ColumnAlignments.js":
/*!***********************************************************************!*\
  !*** ./lib/plugins/gridtables/common/markdown-it/ColumnAlignments.js ***!
  \***********************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Bas Verweij. All rights reserved.
 *  Licensed under the MIT License. See LICENSE in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
var ColumnAlignments;
(function (ColumnAlignments) {
    ColumnAlignments["None"] = "";
    ColumnAlignments["Left"] = "left";
    ColumnAlignments["Center"] = "center";
    ColumnAlignments["Right"] = "right";
})(ColumnAlignments || (ColumnAlignments = {}));
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (ColumnAlignments);


/***/ }),

/***/ "./lib/plugins/gridtables/common/markdown-it/EmitTable.js":
/*!****************************************************************!*\
  !*** ./lib/plugins/gridtables/common/markdown-it/EmitTable.js ***!
  \****************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ emitTable)
/* harmony export */ });
/* harmony import */ var _gridtables_GetCells__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../gridtables/GetCells */ "./lib/plugins/gridtables/common/gridtables/GetCells.js");
/* harmony import */ var _ColumnAlignments__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./ColumnAlignments */ "./lib/plugins/gridtables/common/markdown-it/ColumnAlignments.js");
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Bas Verweij. All rights reserved.
 *  Licensed under the MIT License. See LICENSE in the project root for license information.
 *--------------------------------------------------------------------------------------------*/


function emitTable(md, state, result) {
    let offsets = result.SeparatorLineOffsets;
    let token = state.push('table_open', 'table', 1);
    token.map = [offsets[0], offsets[offsets.length - 1]];
    if (result.HeaderLines.length > 0) {
        // emit table header
        const token = state.push('thead_open', 'thead', 1);
        token.map = [offsets[0], offsets[1]];
        const cells = (0,_gridtables_GetCells__WEBPACK_IMPORTED_MODULE_0__["default"])(result.HeaderLines);
        processRow(md, state, 'th', result.ColumnAlignments, offsets[0], offsets[1], cells);
        state.push('thead_close', 'thead', -1);
        offsets = offsets.slice(1);
    }
    // emit table body
    token = state.push('tbody_open', 'tbody', 1);
    token.map = [offsets[0], offsets[offsets.length - 1]];
    for (let i = 0; i < result.RowLines.length; i++) {
        let cells = (0,_gridtables_GetCells__WEBPACK_IMPORTED_MODULE_0__["default"])(result.RowLines[i]);
        processRow(md, state, 'td', result.ColumnAlignments, offsets[i], offsets[i + 1], cells);
    }
    state.push('tbody_close', 'tbody', -1);
    state.push('table_close', 'table', -1);
}
function processRow(md, state, tag, columnAlignments, lineBegin, lineEnd, cells) {
    let token = state.push('tr_open', 'tr', 1);
    token.map = [lineBegin, lineEnd];
    for (let i = 0; i < cells.length; i++) {
        let token = state.push(tag + '_open', tag, 1);
        token.map = [lineBegin + 1, lineEnd - 1];
        if (columnAlignments[i] !== _ColumnAlignments__WEBPACK_IMPORTED_MODULE_1__["default"].None) {
            token.attrSet("style", `text-align: ${columnAlignments[i]};`);
        }
        if (cells[i].length === 0) {
            // empty cell
        }
        else if (cells[i].length === 1) {
            // single line cell -> emit as inline markdown
            let token = state.push('inline', '', 0);
            token.content = cells[i][0].trim();
            token.children = [];
        }
        else {
            // multi line cell -> render and emit as html
            let cell = md
                .render(cells[i].join('\r\n'))
                .trim();
            // remove single p tag because we're in a table cell
            if ((cell.slice(0, 3) === '<p>') &&
                (cell.slice(-4) === '</p>') &&
                (cell.indexOf('<p>', 3) === -1)) {
                cell = cell.slice(3, cell.length - 4);
            }
            let token = state.push('html_block', '', 0);
            token.content = cell;
            token.children = [];
        }
        state.push(tag + '_close', tag, -1);
    }
    state.push('tr_close', 'tr', -1);
}


/***/ }),

/***/ "./lib/plugins/gridtables/common/markdown-it/GetCharCodeAtStartOfLine.js":
/*!*******************************************************************************!*\
  !*** ./lib/plugins/gridtables/common/markdown-it/GetCharCodeAtStartOfLine.js ***!
  \*******************************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ getCharCodeAtStartOfLine)
/* harmony export */ });
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Bas Verweij. All rights reserved.
 *  Licensed under the MIT License. See LICENSE in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
/**
 * Returns the char code of the character at the start of the current line,
 * or -1 if this is not available (e.g. on an empty line).
 *
 * @param state The Markdown It state.
 */
function getCharCodeAtStartOfLine(state, line) {
    const pos = state.bMarks[line] +
        state.tShift[line];
    if (pos >= state.eMarks[line]) {
        return -1;
    }
    return state.src.charCodeAt(pos);
}


/***/ }),

/***/ "./lib/plugins/gridtables/common/markdown-it/GetLine.js":
/*!**************************************************************!*\
  !*** ./lib/plugins/gridtables/common/markdown-it/GetLine.js ***!
  \**************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ getLine)
/* harmony export */ });
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Bas Verweij. All rights reserved.
 *  Licensed under the MIT License. See LICENSE in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
function getLine(state, line) {
    const start = state.bMarks[line] + state.blkIndent;
    const end = state.eMarks[line];
    return state.src.substr(start, end - start);
}


/***/ }),

/***/ "./lib/plugins/gridtables/common/markdown-it/ParseTable.js":
/*!*****************************************************************!*\
  !*** ./lib/plugins/gridtables/common/markdown-it/ParseTable.js ***!
  \*****************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ parseTable)
/* harmony export */ });
/* harmony import */ var wcwidth__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! wcwidth */ "webpack/sharing/consume/default/wcwidth/wcwidth");
/* harmony import */ var wcwidth__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(wcwidth__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _gridtables_GetColumnWidths__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../gridtables/GetColumnWidths */ "./lib/plugins/gridtables/common/gridtables/GetColumnWidths.js");
/* harmony import */ var _ColumnAlignments__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./ColumnAlignments */ "./lib/plugins/gridtables/common/markdown-it/ColumnAlignments.js");
/* harmony import */ var _GetLine__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./GetLine */ "./lib/plugins/gridtables/common/markdown-it/GetLine.js");
/* harmony import */ var _ParseTableResult__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./ParseTableResult */ "./lib/plugins/gridtables/common/markdown-it/ParseTableResult.js");
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Bas Verweij. All rights reserved.
 *  Licensed under the MIT License. See LICENSE in the project root for license information.
 *--------------------------------------------------------------------------------------------*/





function parseTable(state, startLine, endLine) {
    const result = new _ParseTableResult__WEBPACK_IMPORTED_MODULE_1__["default"]();
    let rowLine = (0,_GetLine__WEBPACK_IMPORTED_MODULE_2__["default"])(state, startLine);
    if (rowLine.charAt(0) !== '+') {
        // line does not start with a '+'
        return result;
    }
    result.ColumnWidths = (0,_gridtables_GetColumnWidths__WEBPACK_IMPORTED_MODULE_3__["default"])(rowLine);
    if (result.ColumnWidths.length === 0) {
        // no columns found
        return result;
    }
    // initialize column alignments
    result.ColumnAlignments = result.ColumnWidths
        .map(_ => _ColumnAlignments__WEBPACK_IMPORTED_MODULE_4__["default"].None);
    if (rowLine.indexOf(':') >= 0) {
        // column alignment specifiers present in first row line
        result.HeaderLess = true;
        // set column alignments
        result.ColumnAlignments = getColumnAlignments(rowLine, result.ColumnWidths);
        // remove alignment specifiers for further matching
        rowLine = rowLine.replace(/[:]/g, '-');
    }
    // create header line matcher
    const headerLineMatcher = new RegExp('^\\+' +
        result.ColumnWidths
            .map(w => `[=:][=]{${w - 3}}[=:]\\+`)
            .join('') +
        '$');
    // build column offsets
    result.ColumnOffsets = [0];
    for (let i = 0; i < result.ColumnWidths.length - 1; i++) {
        result.ColumnOffsets.push(result.ColumnOffsets[i] +
            result.ColumnWidths[i]);
    }
    // create cell line matcher
    const cellLineMatcher = new RegExp('^\\|' +
        result.ColumnWidths
            .map(w => `([^|]{${Math.ceil((w - 1) / 2)},${w - 1}})\\|`)
            .join('') +
        '$');
    // save first separator line offset
    result.SeparatorLineOffsets.push(startLine);
    // continue to scan until a complete table is found, or an invalid line is encountered
    let currentRow = [];
    let currentLine = startLine + 1;
    for (; currentLine <= endLine; currentLine++) {
        const line = (0,_GetLine__WEBPACK_IMPORTED_MODULE_2__["default"])(state, currentLine);
        if (line.charCodeAt(0) === 0x2B) // '+'
         {
            // separator line
            if (currentRow.length === 0) {
                // no row lines since last separator -> invalid table
                return result;
            }
            // save separator line offset
            result.SeparatorLineOffsets.push(currentLine);
            if (line === rowLine) {
                // new regular row
                result.RowLines.push(currentRow);
                if (result.HeaderLines.length === 0) {
                    result.HeaderLess = true;
                }
            }
            else if (!result.HeaderLess &&
                line.match(headerLineMatcher)) {
                // found header line
                if (result.HeaderLines.length > 0 ||
                    result.RowLines.length > 0) {
                    // header already found, or not the first row -> invalid table
                    return result;
                }
                // header row
                result.HeaderLines = currentRow;
                if (line.indexOf(':') >= 0) {
                    // set column alignments
                    result.ColumnAlignments = getColumnAlignments(line, result.ColumnWidths);
                }
            }
            else {
                // not a header or regular row -> invalid table
                return result;
            }
            // reset current row
            currentRow = [];
        }
        else if (line.charCodeAt(0) === 0x7C) // '|'
         {
            // cell line
            const matches = line.match(cellLineMatcher);
            if (matches === null) {
                // cell line does not match -> invalid table
                return result;
            }
            const cells = validateColumnWidths(matches, result.ColumnWidths);
            if (cells === null) {
                // cell line does not match -> invalid table
                return result;
            }
            // add the line to the current row
            currentRow.push(cells);
        }
        else {
            // not a separator or cell line, check if we have a complete table
            if (currentRow.length === 0 &&
                ((result.HeaderLines.length > 0) ||
                    (result.RowLines.length > 0))) {
                // found a complete table
                break;
            }
            return result;
        }
    }
    result.CurrentLine = currentLine;
    result.Success = true;
    return result;
}
function getColumnAlignments(line, columnWidths) {
    let alignments = [];
    let left = 1;
    let right = -1;
    for (let i = 0; i < columnWidths.length; i++) {
        right += columnWidths[i];
        let alignment = _ColumnAlignments__WEBPACK_IMPORTED_MODULE_4__["default"].None;
        if (line.charAt(right) === ':') {
            if (line.charAt(left) === ':') {
                alignment = _ColumnAlignments__WEBPACK_IMPORTED_MODULE_4__["default"].Center;
            }
            else {
                alignment = _ColumnAlignments__WEBPACK_IMPORTED_MODULE_4__["default"].Right;
            }
        }
        else if (line.charAt(left) === ':') {
            alignment = _ColumnAlignments__WEBPACK_IMPORTED_MODULE_4__["default"].Left;
        }
        alignments.push(alignment);
        left += columnWidths[i];
    }
    return alignments;
}
function validateColumnWidths(matches, columnWidths) {
    const cells = [];
    for (var i = 0; i < columnWidths.length; i++) {
        const cell = matches[i + 1];
        const columnWidth = wcwidth__WEBPACK_IMPORTED_MODULE_0___default()(cell) + 1; // add 1 for separator
        if (columnWidth !== columnWidths[i]) {
            return null;
        }
        cells.push(cell);
    }
    return cells;
}


/***/ }),

/***/ "./lib/plugins/gridtables/common/markdown-it/ParseTableResult.js":
/*!***********************************************************************!*\
  !*** ./lib/plugins/gridtables/common/markdown-it/ParseTableResult.js ***!
  \***********************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ ParseTableResult)
/* harmony export */ });
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Bas Verweij. All rights reserved.
 *  Licensed under the MIT License. See LICENSE in the project root for license information.
 *--------------------------------------------------------------------------------------------*/
class ParseTableResult {
    constructor() {
        this.Success = false;
        this.ColumnWidths = [];
        this.ColumnOffsets = [];
        this.ColumnAlignments = [];
        this.HeaderLess = false;
        this.HeaderLines = [];
        this.RowLines = [];
        this.SeparatorLineOffsets = [];
        this.CurrentLine = 0;
    }
}


/***/ }),

/***/ "./lib/plugins/gridtables/index.js":
/*!*****************************************!*\
  !*** ./lib/plugins/gridtables/index.js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ gridTableRulePlugin)
/* harmony export */ });
/* harmony import */ var _rules_gridtable__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./rules/gridtable */ "./lib/plugins/gridtables/rules/gridtable.js");
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Bas Verweij. All rights reserved.
 *  Licensed under the MIT License. See LICENSE in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

function gridTableRulePlugin(
// eslint-disable-next-line @typescript-eslint/no-explicit-any
md) {
    md.block.ruler.before("table", "gridtable", (0,_rules_gridtable__WEBPACK_IMPORTED_MODULE_0__["default"])(md));
}


/***/ }),

/***/ "./lib/plugins/gridtables/rules/gridtable.js":
/*!***************************************************!*\
  !*** ./lib/plugins/gridtables/rules/gridtable.js ***!
  \***************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ gridTableRule)
/* harmony export */ });
/* harmony import */ var _common_markdown_it_EmitTable__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../common/markdown-it/EmitTable */ "./lib/plugins/gridtables/common/markdown-it/EmitTable.js");
/* harmony import */ var _common_markdown_it_GetCharCodeAtStartOfLine__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../common/markdown-it/GetCharCodeAtStartOfLine */ "./lib/plugins/gridtables/common/markdown-it/GetCharCodeAtStartOfLine.js");
/* harmony import */ var _common_markdown_it_ParseTable__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../common/markdown-it/ParseTable */ "./lib/plugins/gridtables/common/markdown-it/ParseTable.js");
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Bas Verweij. All rights reserved.
 *  Licensed under the MIT License. See LICENSE in the project root for license information.
 *--------------------------------------------------------------------------------------------*/



function gridTableRule(md) {
    return function (state, startLine, endLine, silent) {
        if ((0,_common_markdown_it_GetCharCodeAtStartOfLine__WEBPACK_IMPORTED_MODULE_0__["default"])(state, startLine) !== 0x2B) {
            // line does not start with a '+'
            return false;
        }
        let parseResult = (0,_common_markdown_it_ParseTable__WEBPACK_IMPORTED_MODULE_1__["default"])(state, startLine, endLine);
        if (!parseResult.Success) {
            return false;
        }
        if (silent) {
            return true;
        }
        (0,_common_markdown_it_EmitTable__WEBPACK_IMPORTED_MODULE_2__["default"])(md, state, parseResult);
        state.line = parseResult.CurrentLine;
        return true;
    };
}


/***/ }),

/***/ "./lib/plugins/math.js":
/*!*****************************!*\
  !*** ./lib/plugins/math.js ***!
  \*****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "kTokMathBlock": () => (/* binding */ kTokMathBlock),
/* harmony export */   "kTokMathInline": () => (/* binding */ kTokMathInline),
/* harmony export */   "mathjaxPlugin": () => (/* binding */ mathjaxPlugin)
/* harmony export */ });
/*
 * math.ts
 *
 * Copyright (C) 2020-2023 Posit Software, PBC
 *
 */
const kTokMathBlock = "math_block";
const kTokMathInline = "math_inline";
function renderMath(content, convertOptions) {
    if (convertOptions.display) {
        return `<div class='quarto-display-math'>\\[${content}\\]</div>`;
    }
    else {
        return `<span class='quarto-inline-math'>\\(${content}\\)</span>`;
    }
}
// Test if potential opening or closing delimieter
// Assumes that there is a "$" at state.src[pos]
function isValidDelim(state, pos) {
    const max = state.posMax;
    let can_open = true;
    let can_close = true;
    const prevChar = pos > 0 ? state.src.charCodeAt(pos - 1) : -1, nextChar = pos + 1 <= max ? state.src.charCodeAt(pos + 1) : -1;
    // Check non-whitespace conditions for opening and closing, and
    // check that closing delimeter isn't followed by a number
    if (prevChar === 0x20 /* " " */ ||
        prevChar === 0x09 /* \t */ ||
        (nextChar >= 0x30 /* "0" */ && nextChar <= 0x39) /* "9" */) {
        can_close = false;
    }
    if (nextChar === 0x20 /* " " */ || nextChar === 0x09 /* \t */) {
        can_open = false;
    }
    return {
        can_open: can_open,
        can_close: can_close,
    };
}
function math_inline(state, silent) {
    if (state.src[state.pos] !== "$") {
        return false;
    }
    let res = isValidDelim(state, state.pos);
    if (!res.can_open) {
        if (!silent) {
            state.pending += "$";
        }
        state.pos += 1;
        return true;
    }
    // First check for and bypass all properly escaped delimieters
    // This loop will assume that the first leading backtick can not
    // be the first character in state.src, which is known since
    // we have found an opening delimieter already.
    const start = state.pos + 1;
    let match = start;
    while ((match = state.src.indexOf("$", match)) !== -1) {
        // Found potential $, look for escapes, pos will point to
        // first non escape when complete
        let pos = match - 1;
        while (state.src[pos] === "\\") {
            pos -= 1;
        }
        // Even number of escapes, potential closing delimiter found
        if ((match - pos) % 2 == 1) {
            break;
        }
        match += 1;
    }
    // No closing delimter found.  Consume $ and continue.
    if (match === -1) {
        if (!silent) {
            state.pending += "$";
        }
        state.pos = start;
        return true;
    }
    // Check if we have empty content, ie: $$.  Do not parse.
    if (match - start === 0) {
        if (!silent) {
            state.pending += "$$";
        }
        state.pos = start + 1;
        return true;
    }
    // Check for valid closing delimiter
    res = isValidDelim(state, match);
    if (!res.can_close) {
        if (!silent) {
            state.pending += "$";
        }
        state.pos = start;
        return true;
    }
    if (!silent) {
        const token = state.push("math_inline", "math", 0);
        token.markup = "$";
        token.content = state.src.slice(start, match);
    }
    state.pos = match + 1;
    return true;
}
function math_block(state, start, end, silent) {
    let next, lastPos;
    let found = false, pos = state.bMarks[start] + state.tShift[start], max = state.eMarks[start], lastLine = "";
    if (pos + 2 > max) {
        return false;
    }
    if (state.src.slice(pos, pos + 2) !== "$$") {
        return false;
    }
    pos += 2;
    let firstLine = state.src.slice(pos, max);
    if (silent) {
        return true;
    }
    if (firstLine.trim().slice(-2) === "$$") {
        // Single line expression
        firstLine = firstLine.trim().slice(0, -2);
        found = true;
    }
    let attrStr = undefined;
    for (next = start; !found;) {
        next++;
        if (next >= end) {
            break;
        }
        pos = state.bMarks[next] + state.tShift[next];
        max = state.eMarks[next];
        if (pos < max && state.tShift[next] < state.blkIndent) {
            // non-empty line with negative indent should stop the list:
            break;
        }
        const line = state.src.slice(pos, max).trim();
        const match = line.match(/^\$\$\s*(\{.*\})?\s*$/);
        if (match) {
            lastPos = state.src.slice(0, max).lastIndexOf("$$");
            lastLine = state.src.slice(pos, lastPos);
            attrStr = match[1];
            found = true;
        }
    }
    state.line = next + 1;
    const token = state.push(kTokMathBlock, "math", 0);
    token.block = true;
    if (attrStr) {
        token.info = attrStr;
    }
    token.content =
        (firstLine && firstLine.trim() ? firstLine + "\n" : "") +
            state.getLines(start + 1, next, state.tShift[start], true) +
            (lastLine && lastLine.trim() ? lastLine : "");
    token.map = [start, state.line];
    token.markup = "$$";
    return true;
}
function mathjaxPlugin(md) {
    // Default options
    const convertOptions = {
        display: false
    };
    // set MathJax as the renderer for markdown-it-simplemath
    md.inline.ruler.after("escape", kTokMathInline, math_inline);
    md.block.ruler.after("blockquote", kTokMathBlock, math_block, {
        alt: ["paragraph", "reference", "blockquote", "list"],
    });
    md.renderer.rules.math_inline = function (tokens, idx) {
        convertOptions.display = false;
        return renderMath(tokens[idx].content, convertOptions);
    };
    md.renderer.rules.math_block = function (tokens, idx) {
        convertOptions.display = true;
        return renderMath(tokens[idx].content, convertOptions);
    };
}
;


/***/ }),

/***/ "./lib/plugins/mermaid/index.js":
/*!**************************************!*\
  !*** ./lib/plugins/mermaid/index.js ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ mermaidPlugin)
/* harmony export */ });
/* harmony import */ var mermaid__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! mermaid */ "webpack/sharing/consume/default/mermaid/mermaid");
/* harmony import */ var mermaid__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(mermaid__WEBPACK_IMPORTED_MODULE_0__);

function mermaidPlugin(md, options) {
    const kLang = "mermaid";
    const kContainer = "quarto-mermaid";
    mermaid__WEBPACK_IMPORTED_MODULE_0___default().initialize({
        securityLevel: "loose",
        theme: options.dark ? "dark" : "default",
        ...options,
    });
    const defaultFenceRenderer = md.renderer.rules.fence;
    // Render custom code types as SVGs, letting the fence parser do all the heavy lifting.
    function mermaidFenceRenderer(tokens, idx, options, env, slf) {
        const token = tokens[idx];
        if (token.info === kLang || (token.attrs !== null && token.attrs.length === 1 && token.attrs[0][0] === kLang)) {
            let imageHTML = "";
            const imageAttrs = [];
            // Create element to render into
            const element = document.createElement("div");
            document.body.appendChild(element);
            // Render with Mermaid
            try {
                mermaid__WEBPACK_IMPORTED_MODULE_0___default().mermaidAPI.render(kContainer, token.content, (html) => {
                    // We need to forcibly extract the max-width/height attributes to set on img tag
                    const mermaidEl = document.getElementById(kContainer);
                    if (mermaidEl !== null) {
                        imageAttrs.push([
                            "style",
                            `max-width:${mermaidEl.style.maxWidth};max-height:${mermaidEl.style.maxHeight}`,
                        ]);
                    }
                    // Store HTML
                    imageHTML = html;
                }, element);
            }
            catch (e) {
                return `<pre>Failed to render mermaid diagram.${e}</pre>`;
            }
            finally {
                element.remove();
            }
            // Store encoded image data
            imageAttrs.push(["src", `data:image/svg+xml,${encodeURIComponent(imageHTML)}`]);
            return `<img ${slf.renderAttrs({ attrs: imageAttrs })}>`;
        }
        else {
            if (defaultFenceRenderer !== undefined) {
                return defaultFenceRenderer(tokens, idx, options, env, slf);
            }
            // Missing fence renderer!
            return "";
        }
    }
    md.renderer.rules.fence = mermaidFenceRenderer;
}


/***/ }),

/***/ "./lib/plugins/shortcodes.js":
/*!***********************************!*\
  !*** ./lib/plugins/shortcodes.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "kShortcode": () => (/* binding */ kShortcode),
/* harmony export */   "shortcodePlugin": () => (/* binding */ shortcodePlugin)
/* harmony export */ });
/* harmony import */ var markdown_it_lib_common_utils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! markdown-it/lib/common/utils */ "../../node_modules/markdown-it/lib/common/utils.js");

const kShortcode = "shortcode";
const shortcodePlugin = (md) => {
    const shortcode = (state, silent) => {
        // {{< shortcode >}}
        if (state.src.slice(state.pos, state.pos + 3) !== "{{<") {
            return false;
        }
        const shortcodeEndRegex = />}}/g;
        // ignore if shortcode doesn't end
        const end = state.src.slice(state.pos).search(shortcodeEndRegex);
        if (end === -1) {
            return false;
        }
        const shortcodeContent = state.src.slice(state.pos + 3, state.pos + end);
        if (!silent) {
            const token = state.push("shortcode", "shortcode", 0);
            token.markup = "";
            token.content = shortcodeContent;
        }
        state.pos += end + 3;
        return true;
    };
    md.inline.ruler.after("escape", kShortcode, shortcode);
    const renderShortcode = (tokens, idx) => {
        const token = tokens[idx];
        const content = token.content;
        // insert shortcode braces and escape content's html entities
        return `<span class="shortcode">${(0,markdown_it_lib_common_utils__WEBPACK_IMPORTED_MODULE_0__.escapeHtml)(`{{<${content}>}}`)}</span>`;
    };
    md.renderer.rules[kShortcode] = renderShortcode;
};


/***/ }),

/***/ "./lib/plugins/spans.js":
/*!******************************!*\
  !*** ./lib/plugins/spans.js ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "spansPlugin": () => (/* binding */ spansPlugin)
/* harmony export */ });
/*
 * span.ts
 *
 * Copyright (C) 2020-2023 Posit Software, PBC
 *
 */
function spansPlugin(md) {
    function span(state) {
        const max = state.posMax;
        if (state.src.charCodeAt(state.pos) !== 0x5B) {
            // opening [
            return false;
        }
        const labelStart = state.pos + 1;
        const labelEnd = state.md.helpers.parseLinkLabel(state, state.pos, true);
        if (labelEnd < 0) {
            // parser failed to find closing ]
            return false;
        }
        const pos = labelEnd + 1;
        if (pos < max && state.src.charCodeAt(pos) === 0x7B /* { */) {
            // probably found span
            state.pos = labelStart;
            state.posMax = labelEnd;
            state.push('span_open', 'span', 1);
            state.md.inline.tokenize(state);
            state.push('span_close', 'span', -1);
            state.pos = pos;
            state.posMax = max;
            return true;
        }
        else {
            return false;
        }
    }
    ;
    md.inline.ruler.push('quarto-spans', span);
}


/***/ }),

/***/ "./lib/plugins/table-captions.js":
/*!***************************************!*\
  !*** ./lib/plugins/table-captions.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "tableCaptionPlugin": () => (/* binding */ tableCaptionPlugin)
/* harmony export */ });
/* harmony import */ var _utils_tok__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./utils/tok */ "./lib/plugins/utils/tok.js");
/*
 * table-captions.ts
 *
 * Copyright (C) 2020-2023 Posit Software, PBC
 *
 */

const kTableCaptionRule = "quarto-table-captions";
const tableCaptionPlugin = (md) => {
    md.core.ruler.push(kTableCaptionRule, (state) => {
        const tableIdxs = [];
        const tablePoss = [];
        // Identify tables that we'd like to process
        // The tables must be the bottom first (we will process them bottom to
        // top to ensure that the positions remain accurate as the tokens
        // are mutated
        for (let i = 0; i < state.tokens.length; i++) {
            const token = state.tokens[i];
            if (token.type === _utils_tok__WEBPACK_IMPORTED_MODULE_0__.kTokTableOpen) {
                tableIdxs.push(i);
            }
            else if (token.type === _utils_tok__WEBPACK_IMPORTED_MODULE_0__.kTokTableClose) {
                const start = tableIdxs.pop();
                if (start) {
                    tablePoss.unshift({
                        start,
                        end: i
                    });
                }
            }
        }
        // Look just past the tables and if there is a paragraph that is 
        // a table caption, extract that and place it in the table      
        for (const tablePos of tablePoss) {
            resolveTableCaption(state.tokens, tablePos.start, tablePos.end);
        }
    });
};
function resolveTableCaption(tokens, tblStartPos, tblEndPos) {
    // Must have at least three tokens past the table end
    if (tokens.length > tblEndPos + 3) {
        if (tokens[tblEndPos + 1].type === _utils_tok__WEBPACK_IMPORTED_MODULE_0__.kTokParaOpen
            && tokens[tblEndPos + 2].type === _utils_tok__WEBPACK_IMPORTED_MODULE_0__.kTokInline
            && tokens[tblEndPos + 3].type === _utils_tok__WEBPACK_IMPORTED_MODULE_0__.kTokParaClose) {
            const maybeCaption = tokens[tblEndPos + 2];
            const isText = maybeCaption.children !== null && maybeCaption.children.length > 0 && maybeCaption.children[0].type === _utils_tok__WEBPACK_IMPORTED_MODULE_0__.kTokText;
            const maybeCaptionText = isText ? maybeCaption.children[0].content : "";
            const match = maybeCaptionText.match(/^:\s([^{}]*)(?:\{.*\}){0,1}$/);
            if (match && match[1]) {
                // Carve out the existing tokens
                const capTokens = tokens.splice(tblEndPos + 1, 3);
                // We have the caption, remove the paragraph and return
                // the caption
                capTokens[0].type = "table_caption";
                capTokens[0].tag = "caption";
                // Forward any attributes from the caption up to the table
                tokens[tblStartPos].attrs = capTokens[0].attrs;
                capTokens[0].attrs = [];
                // Trim the content
                capTokens[1].children[0].content = match[1];
                // Close the caption
                capTokens[2].type = "table_caption";
                capTokens[2].tag = "caption";
                tokens.splice(tblStartPos + 1, 0, ...capTokens);
            }
        }
    }
}


/***/ }),

/***/ "./lib/plugins/utils/html.js":
/*!***********************************!*\
  !*** ./lib/plugins/utils/html.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "attributeDecorator": () => (/* binding */ attributeDecorator),
/* harmony export */   "decorator": () => (/* binding */ decorator)
/* harmony export */ });
/* harmony import */ var _markdownit__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./markdownit */ "./lib/plugins/utils/markdownit.js");
/*
* html.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/

const decorator = (contents, customClass) => {
    if (contents.length > 0) {
        // Provide a decorator with the attributes
        return `<div class="quarto-attribute-decorator${customClass ? ' ' + customClass : ""}">${contents.map(decoratorSpan).join("")}</div>`;
    }
    else {
        // There is no decorator - no attributes
        return "";
    }
};
const attributeDecorator = (token, options) => {
    var _a;
    // id
    const id = (0,_markdownit__WEBPACK_IMPORTED_MODULE_0__.readAttrValue)("id", token.attrs);
    // classes
    const clz = (0,_markdownit__WEBPACK_IMPORTED_MODULE_0__.readAttrValue)("class", token.attrs);
    // other attributes
    const otherAttrs = (_a = token.attrs) === null || _a === void 0 ? void 0 : _a.filter((attr) => { return attr[0] !== "id" && attr[0] !== "class"; });
    // Create a decorator for the div
    const contents = [];
    if (id && !(options === null || options === void 0 ? void 0 : options.hide.id)) {
        contents.push(`#${id}`);
    }
    if (clz && !(options === null || options === void 0 ? void 0 : options.hide.classes)) {
        const clzStr = clz.split(" ").map((cls) => `.${cls}`).join(" ");
        contents.push(clzStr);
    }
    if (otherAttrs && otherAttrs.length > 0 && !(options === null || options === void 0 ? void 0 : options.hide.attributes)) {
        const otherAttrStr = otherAttrs === null || otherAttrs === void 0 ? void 0 : otherAttrs.map((attr) => {
            return `${attr[0]}="${attr[1]}"`;
        }).join(" ");
        contents.push(otherAttrStr);
    }
    return decorator(contents, options === null || options === void 0 ? void 0 : options.customClass);
};
const decoratorSpan = (contents) => {
    return `<span class="quarto-attribute-decorator-content">${contents}</span>`;
};


/***/ }),

/***/ "./lib/plugins/utils/markdownit.js":
/*!*****************************************!*\
  !*** ./lib/plugins/utils/markdownit.js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "addClass": () => (/* binding */ addClass),
/* harmony export */   "hasClass": () => (/* binding */ hasClass),
/* harmony export */   "readAttrValue": () => (/* binding */ readAttrValue)
/* harmony export */ });
/*
* markdownit.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/
const hasClass = (clz, attrs) => {
    if (attrs === null) {
        return false;
    }
    const classes = readAttrValue("class", attrs);
    if (classes === null) {
        return false;
    }
    else {
        return classes === null || classes === void 0 ? void 0 : classes.split(" ").includes(clz);
    }
};
const readAttrValue = (name, attrs) => {
    if (attrs === null) {
        return undefined;
    }
    const attr = attrs.find((attr) => { return attr[0] === name; });
    return attr ? attr[1] : undefined;
};
const addClass = (clz, attrs) => {
    if (attrs === null) {
        attrs = [];
        attrs.push(["class", clz]);
        return attrs;
    }
    else {
        const clzIdx = attrs.findIndex((attr) => attr[0] === "class");
        if (clzIdx >= 0) {
            const currentClz = attrs[clzIdx];
            attrs[clzIdx] = ["class", `${currentClz[1]} ${clz}`.trim()];
            return attrs;
        }
        else {
            attrs.push(["class", clz]);
            return attrs;
        }
    }
};


/***/ }),

/***/ "./lib/plugins/utils/tok.js":
/*!**********************************!*\
  !*** ./lib/plugins/utils/tok.js ***!
  \**********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "kTokHeadingOpen": () => (/* binding */ kTokHeadingOpen),
/* harmony export */   "kTokInline": () => (/* binding */ kTokInline),
/* harmony export */   "kTokParaClose": () => (/* binding */ kTokParaClose),
/* harmony export */   "kTokParaOpen": () => (/* binding */ kTokParaOpen),
/* harmony export */   "kTokTableClose": () => (/* binding */ kTokTableClose),
/* harmony export */   "kTokTableOpen": () => (/* binding */ kTokTableOpen),
/* harmony export */   "kTokText": () => (/* binding */ kTokText)
/* harmony export */ });
/*
* tok.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/
const kTokParaOpen = "paragraph_open";
const kTokParaClose = "paragraph_close";
const kTokInline = "inline";
const kTokTableOpen = "table_open";
const kTokTableClose = "table_close";
const kTokText = "text";
const kTokHeadingOpen = "heading_open";


/***/ }),

/***/ "./lib/plugins/yaml.js":
/*!*****************************!*\
  !*** ./lib/plugins/yaml.js ***!
  \*****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "yamlPlugin": () => (/* binding */ yamlPlugin)
/* harmony export */ });
/* harmony import */ var js_yaml__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! js-yaml */ "webpack/sharing/consume/default/js-yaml/js-yaml");
/* harmony import */ var js_yaml__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(js_yaml__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _utils_html__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./utils/html */ "./lib/plugins/utils/html.js");
/*
 * markdownit-yaml.ts
 *
 * Copyright (C) 2022 by Posit Software, PBC
 * Copyright (c) 2016-2020 ParkSB.
 *
 * Unless you have received this program directly from Posit Software pursuant
 * to the terms of a commercial license agreement with Posit Software, then
 * this program is licensed to you under the terms of version 3 of the
 * GNU Affero General Public License. This program is distributed WITHOUT
 * ANY EXPRESS OR IMPLIED WARRANTY, INCLUDING THOSE OF NON-INFRINGEMENT,
 * MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. Please refer to the
 * AGPL (http://www.gnu.org/licenses/agpl-3.0.txt) for more details.
 *
 */


// Typescript version of https://github.com/parksb/markdown-it-front-matter
// TODO: Rationalize this with quarto-core/src/markdownit-yaml.ts
//       This is a copy with rendering added - the core tokenizing function is identical (or should be)
const kTokFrontMatter = 'front_matter';
function yamlPlugin(md, cb) {
    const min_markers = 3, marker_str = "-", marker_char = marker_str.charCodeAt(0), marker_len = marker_str.length;
    function frontMatter(state, startLine, endLine, silent) {
        let pos, nextLine, start_content, auto_closed = false, start = state.bMarks[startLine] + state.tShift[startLine], max = state.eMarks[startLine];
        // Check out the first character of the first line quickly,
        // this should filter out non-front matter
        if (startLine !== 0 || marker_char !== state.src.charCodeAt(0)) {
            return false;
        }
        // Check out the rest of the marker string
        // while pos <= 3
        for (pos = start + 1; pos <= max; pos++) {
            if (marker_str[(pos - start) % marker_len] !== state.src[pos]) {
                start_content = pos + 1;
                break;
            }
        }
        const marker_count = Math.floor((pos - start) / marker_len);
        if (marker_count < min_markers) {
            return false;
        }
        pos -= (pos - start) % marker_len;
        // Since start is found, we can report success here in validation mode
        if (silent) {
            return true;
        }
        // Search for the end of the block
        nextLine = startLine;
        for (;;) {
            nextLine++;
            if (nextLine >= endLine) {
                // unclosed block should be autoclosed by end of document.
                // also block seems to be autoclosed by end of parent
                break;
            }
            if (state.src.slice(start, max) === "...") {
                break;
            }
            start = state.bMarks[nextLine] + state.tShift[nextLine];
            max = state.eMarks[nextLine];
            if (start < max && state.sCount[nextLine] < state.blkIndent) {
                // non-empty line with negative indent should stop the list:
                // - ```
                //  test
                break;
            }
            if (marker_char !== state.src.charCodeAt(start)) {
                continue;
            }
            if (state.sCount[nextLine] - state.blkIndent >= 4) {
                // closing fence should be indented less than 4 spaces
                continue;
            }
            for (pos = start + 1; pos <= max; pos++) {
                if (marker_str[(pos - start) % marker_len] !== state.src[pos]) {
                    break;
                }
            }
            // closing code fence must be at least as long as the opening one
            if (Math.floor((pos - start) / marker_len) < marker_count) {
                continue;
            }
            // make sure tail has spaces only
            pos -= (pos - start) % marker_len;
            pos = state.skipSpaces(pos);
            if (pos < max) {
                continue;
            }
            // found!
            auto_closed = true;
            break;
        }
        const old_parent = state.parentType;
        const old_line_max = state.lineMax;
        state.parentType = "root";
        // this will prevent lazy continuations from ever going past our end marker
        state.lineMax = nextLine;
        const token = state.push("front_matter", "", 0);
        token.hidden = true;
        token.markup = state.src.slice(startLine, pos);
        token.block = true;
        token.map = [startLine, pos];
        token.meta = state.src.slice(start_content, start - 1);
        state.parentType = old_parent;
        state.lineMax = old_line_max;
        state.line = nextLine + (auto_closed ? 1 : 0);
        if (cb) {
            cb(token.meta);
        }
        return true;
    }
    md.block.ruler.before("table", kTokFrontMatter, frontMatter, {
        alt: ["paragraph", "reference", "blockquote", "list"],
    });
    // Add rendering
    md.renderer.rules[kTokFrontMatter] = renderFrontMatter;
}
function renderFrontMatter(tokens, idx) {
    const token = tokens[idx];
    // Parse the markup
    const frontUnknown = parseFrontMatterStr(token.markup);
    // Extract important content
    if (typeof (frontUnknown) === "object") {
        const titleBlock = {};
        const frontMatter = frontUnknown;
        const readStr = (key) => {
            if (frontMatter[key] === undefined) {
                return undefined;
            }
            else if (typeof (frontMatter[key]) === "string") {
                const val = frontMatter[key];
                delete frontMatter[key];
                return val;
            }
            else {
                return undefined;
            }
        };
        // Read simple values
        titleBlock.title = readStr("title");
        titleBlock.subtitle = readStr("subtitle");
        titleBlock.abstract = readStr("abstract");
        titleBlock.date = readStr("date");
        titleBlock.modified = readStr("date-modified");
        titleBlock.doi = readStr("doi");
        // Read Authors
        titleBlock.authors = parseAuthor(frontMatter.author || frontMatter.authors);
        delete frontMatter.author;
        delete frontMatter.authors;
        // The final rendered HTML output
        const titleLines = [];
        // Render the title block and other yaml options
        const titleRendered = renderTitle(titleBlock);
        titleLines.push(titleRendered);
        if (Object.keys(frontMatter).length > 0) {
            // decorator
            const decor = (0,_utils_html__WEBPACK_IMPORTED_MODULE_1__.decorator)(["Options"]);
            titleLines.push(decor);
            // yaml
            const yamlDump = js_yaml__WEBPACK_IMPORTED_MODULE_0__.dump(frontMatter);
            const otherYamlRendered = `<pre class="quarto-frontmatter-container"><code class="cm-s-jupyter language-yaml quarto-frontmatter">${yamlDump}</code></pre>`;
            titleLines.push(otherYamlRendered);
        }
        return titleLines.join("\n");
    }
    else {
        return "";
    }
}
// TODO: Use core function instead
function parseFrontMatterStr(str) {
    str = str.replace(/---\s*$/, "");
    try {
        return js_yaml__WEBPACK_IMPORTED_MODULE_0__.load(str, { schema: js_yaml__WEBPACK_IMPORTED_MODULE_0__.FAILSAFE_SCHEMA });
    }
    catch (error) {
        return undefined;
    }
}
function renderTitle(titleBlock) {
    var _a;
    const rendered = [];
    if (titleBlock.title) {
        rendered.push(`<h1>${titleBlock.title}</h1>`);
    }
    if (titleBlock.subtitle) {
        rendered.push(`<p class="quarto-subtitle">${titleBlock.subtitle}</p>`);
    }
    const metadataBlocks = [];
    if (titleBlock.authors && ((_a = titleBlock.authors) === null || _a === void 0 ? void 0 : _a.length) > 0) {
        const names = [];
        const affils = [];
        for (let i = 0; i < titleBlock.authors.length; i++) {
            const author = titleBlock.authors[i];
            if (author.orcid) {
                names.push({
                    value: `${author.name}<a href="https://orcid.org/${author.orcid}" class="quarto-orcid"><i></i></a>`,
                    padded: i > 0
                });
            }
            else {
                names.push({ value: author.name, padded: i > 0 });
            }
            // Place empty rows to allow affiliations to line up
            const emptyCount = author.affil ? Math.max(author.affil.length - 1, 0) : 0;
            for (let j = 0; j < emptyCount; j++) {
                names.push({ value: "&nbsp;" });
            }
            // Collect affilations
            if (author.affil) {
                for (let k = 0; k < author.affil.length; k++) {
                    const affil = author.affil[k];
                    affils.push({
                        value: affil,
                        padded: i > 0 && k == 0
                    });
                }
            }
        }
        const authLabel = names.length === 1 ? "Author" : "Authors";
        metadataBlocks.push(renderDocMeta(authLabel, names));
        if (affils.length > 0) {
            const affilLabel = affils.length === 1 ? "Affiliation" : "Affiliations";
            metadataBlocks.push(renderDocMeta(affilLabel, affils));
        }
    }
    if (titleBlock.date) {
        metadataBlocks.push(renderDocMeta("Date", [{ value: titleBlock.date }]));
    }
    if (titleBlock.modified) {
        metadataBlocks.push(renderDocMeta("Modified", [{ value: titleBlock.modified }]));
    }
    if (titleBlock.doi) {
        metadataBlocks.push(renderDocMeta("DOI", [{ value: `<a href="https://doi.org/${titleBlock.doi}">${titleBlock.doi}</a>` }]));
    }
    if (metadataBlocks.length > 0) {
        rendered.push(renderDocMetas(metadataBlocks));
    }
    if (titleBlock.abstract) {
        rendered.push(`<p class="quarto-abstract">${titleBlock.abstract}</p>`);
    }
    return rendered.join("\n");
}
function renderDocMetas(docMetas) {
    const rendered = [];
    rendered.push(`<div class="quarto-meta-block">`);
    docMetas.forEach((docMeta) => { rendered.push(docMeta); });
    rendered.push(`</div>`);
    return rendered.join("\n");
}
function renderDocMeta(label, vals) {
    const rendered = [];
    rendered.push(`<div class="quarto-meta">`);
    rendered.push(`<p class="quarto-meta-title">${label}</p>`);
    vals.forEach((val) => {
        const clz = val.padded ? ` class="quarto-meta-padded"` : "";
        rendered.push(`<p${clz}>${val.value}</p>`);
    });
    rendered.push(`</div>`);
    return rendered.join("\n");
}
function parseAuthor(author) {
    const authorsRaw = Array.isArray(author) ? author : [author];
    const authors = [];
    for (const authorRaw of authorsRaw) {
        if (typeof (authorRaw) === "string") {
            authors.push({
                name: authorRaw
            });
        }
        else if (typeof (authorRaw) === "object") {
            const str = (key, defaultValue) => {
                if (typeof (authorRaw[key]) === "string") {
                    return authorRaw[key];
                }
                else {
                    return defaultValue;
                }
            };
            const affiliations = [];
            const affiliationSimple = str("affiliation");
            if (affiliationSimple) {
                affiliations.push(affiliationSimple);
            }
            else if (authorRaw.affiliations) {
                const affils = Array.isArray(authorRaw.affiliations) ? authorRaw.affiliations : [authorRaw.affiliations];
                affils.forEach((affilRaw) => {
                    if (typeof (affilRaw) === "string") {
                        affiliations.push(affilRaw);
                        // eslint-disable-next-line no-constant-condition
                    }
                    else if (typeof (affilRaw === "object")) {
                        const affilRecord = affilRaw;
                        const name = affilRecord.name;
                        if (typeof (name) === "string") {
                            affiliations.push(name);
                        }
                    }
                });
            }
            authors.push({
                name: str("name", ""),
                orcid: str("orcid"),
                affil: affiliations
            });
        }
    }
    return authors;
}


/***/ }),

/***/ "./lib/providers/attrs.js":
/*!********************************!*\
  !*** ./lib/providers/attrs.js ***!
  \********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "attrs": () => (/* binding */ attrs)
/* harmony export */ });
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* attrs.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/

const attrs = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/attributes',
    title: 'Markdown Attributes',
    plugin: async () => {
        const plugin = await __webpack_require__.e(/*! import() */ "webpack_sharing_consume_default_markdown-it-attrs_markdown-it-attrs").then(__webpack_require__.t.bind(__webpack_require__, /*! markdown-it-attrs */ "webpack/sharing/consume/default/markdown-it-attrs/markdown-it-attrs", 23));
        return [plugin.default];
    }
});


/***/ }),

/***/ "./lib/providers/callouts.js":
/*!***********************************!*\
  !*** ./lib/providers/callouts.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "callouts": () => (/* binding */ callouts)
/* harmony export */ });
/* harmony import */ var _plugins_callouts__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../plugins/callouts */ "./lib/plugins/callouts.js");
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* callouts.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/


const callouts = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/callouts',
    title: 'Quarto callouts',
    plugin: async () => {
        return [_plugins_callouts__WEBPACK_IMPORTED_MODULE_1__.calloutPlugin];
    }
});


/***/ }),

/***/ "./lib/providers/cites.js":
/*!********************************!*\
  !*** ./lib/providers/cites.js ***!
  \********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "cites": () => (/* binding */ cites)
/* harmony export */ });
/* harmony import */ var _plugins_cites__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../plugins/cites */ "./lib/plugins/cites.js");
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* cites.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/


const cites = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/cites',
    title: 'Citations',
    plugin: async () => {
        return [_plugins_cites__WEBPACK_IMPORTED_MODULE_1__.citationPlugin];
    }
});


/***/ }),

/***/ "./lib/providers/decorator.js":
/*!************************************!*\
  !*** ./lib/providers/decorator.js ***!
  \************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "decorator": () => (/* binding */ decorator)
/* harmony export */ });
/* harmony import */ var _plugins_decorator__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../plugins/decorator */ "./lib/plugins/decorator.js");
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* code.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/


const decorator = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/fence',
    title: 'Fenced Code Blocks',
    plugin: async () => {
        return [_plugins_decorator__WEBPACK_IMPORTED_MODULE_1__.decoratorPlugin];
    }
});


/***/ }),

/***/ "./lib/providers/deflist.js":
/*!**********************************!*\
  !*** ./lib/providers/deflist.js ***!
  \**********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "deflist": () => (/* binding */ deflist)
/* harmony export */ });
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* deflist.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/

const deflist = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/deflist',
    title: 'Definition Lists',
    plugin: async () => {
        const plugin = await __webpack_require__.e(/*! import() */ "webpack_sharing_consume_default_markdown-it-deflist_markdown-it-deflist").then(__webpack_require__.t.bind(__webpack_require__, /*! markdown-it-deflist */ "webpack/sharing/consume/default/markdown-it-deflist/markdown-it-deflist", 23));
        return [plugin.default];
    }
});


/***/ }),

/***/ "./lib/providers/divs.js":
/*!*******************************!*\
  !*** ./lib/providers/divs.js ***!
  \*******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "divs": () => (/* binding */ divs)
/* harmony export */ });
/* harmony import */ var _plugins_divs__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../plugins/divs */ "./lib/plugins/divs.js");
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* callouts.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/


const divs = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/divs',
    title: 'Pandoc fenced divs',
    plugin: async () => {
        return [_plugins_divs__WEBPACK_IMPORTED_MODULE_1__.divPlugin];
    },
    hooks: {
        preParse: {
            run: (content) => {
                // Detect close divs that are directly after text (e.g. not back to back whitespace)
                // and add a whitespace. This will cause the close div to become a 'block' 
                // rather than appearing as the end of the paragraph block
                const blockedDivs = content.replace(kCloseDivNoBlock, `$1\n\n$2`);
                return Promise.resolve(blockedDivs);
            }
        }
    }
});
const kCloseDivNoBlock = /([^\s])\n(:::+(?:\{.*\})?)/gm;


/***/ }),

/***/ "./lib/providers/figure-divs.js":
/*!**************************************!*\
  !*** ./lib/providers/figure-divs.js ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "figureDivs": () => (/* binding */ figureDivs)
/* harmony export */ });
/* harmony import */ var _plugins_figure_divs__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../plugins/figure-divs */ "./lib/plugins/figure-divs.js");
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* figure-divs.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/


const figureDivs = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/figureDivs',
    title: 'Quarto Figure Divs',
    plugin: async () => {
        return [_plugins_figure_divs__WEBPACK_IMPORTED_MODULE_1__.figureDivsPlugin];
    }
});


/***/ }),

/***/ "./lib/providers/figures.js":
/*!**********************************!*\
  !*** ./lib/providers/figures.js ***!
  \**********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "figures": () => (/* binding */ figures)
/* harmony export */ });
/* harmony import */ var _plugins_figures__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../plugins/figures */ "./lib/plugins/figures.js");
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* figures.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/


const figures = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/figures',
    title: 'Quarto figures',
    plugin: async () => {
        return [_plugins_figures__WEBPACK_IMPORTED_MODULE_1__.figuresPlugin, { figcaption: true, copyAttrs: true }];
    }
});


/***/ }),

/***/ "./lib/providers/footnotes.js":
/*!************************************!*\
  !*** ./lib/providers/footnotes.js ***!
  \************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "footnotes": () => (/* binding */ footnotes)
/* harmony export */ });
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* footnotes.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/

const footnotes = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/footnotes',
    title: 'Footnotes',
    plugin: async () => {
        const footnotePlugin = await __webpack_require__.e(/*! import() */ "webpack_sharing_consume_default_markdown-it-footnote_markdown-it-footnote").then(__webpack_require__.t.bind(__webpack_require__, /*! markdown-it-footnote */ "webpack/sharing/consume/default/markdown-it-footnote/markdown-it-footnote", 23));
        return [footnotePlugin.default];
    }
});


/***/ }),

/***/ "./lib/providers/gridtables.js":
/*!*************************************!*\
  !*** ./lib/providers/gridtables.js ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "gridtables": () => (/* binding */ gridtables)
/* harmony export */ });
/* harmony import */ var _plugins_gridtables__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../plugins/gridtables */ "./lib/plugins/gridtables/index.js");
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* gridtables.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/


const gridtables = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/gridtables',
    title: 'Grid Tables',
    plugin: async () => {
        return [_plugins_gridtables__WEBPACK_IMPORTED_MODULE_1__["default"]];
    }
});


/***/ }),

/***/ "./lib/providers/math.js":
/*!*******************************!*\
  !*** ./lib/providers/math.js ***!
  \*******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "math": () => (/* binding */ math)
/* harmony export */ });
/* harmony import */ var _plugins_math__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../plugins/math */ "./lib/plugins/math.js");
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* math.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/


const math = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/math',
    title: 'LaTex Math',
    plugin: async () => {
        return [_plugins_math__WEBPACK_IMPORTED_MODULE_1__.mathjaxPlugin];
    },
    hooks: {
        postRender: {
            run: (node) => {
                // Inject mathjax
                const mathjaxId = "MathJax-script";
                const mathJaxScript = document.getElementById(mathjaxId);
                if (!mathJaxScript) {
                    const configEl = document.createElement("script");
                    configEl.innerText = `

MathJax = {
  svg: {
    fontCache: 'global'
  },
  startup: {
    typeset: false,
    pageReady: () => {
      MathJax.startup.promise.then(() => {

        const typesetMath = (els) => {
          MathJax.startup.promise = MathJax.startup.promise
            .then(() => {
              return MathJax.typesetPromise(els); }
            )
            .catch((err) => console.log('Typeset failed: ' + err.message));
          return MathJax.startup.promise;
        };
        
        const typesetCellObserver = new MutationObserver((mutationList, observer) => { 
          const els = mutationList.map((list) => list.target);          
          const typesetEls = [];
          for (const el of els) {
            const childMathEls = el.querySelectorAll('.quarto-inline-math, .quarto-display-math');
            if (childMathEls && childMathEls.length > 0) {
              typesetEls.push(...childMathEls);
            }
          }
          typesetMath(typesetEls);
        });        

        const containerObserver = new MutationObserver((mutationList, observer) => { 
          const nodes = [];
          mutationList.forEach((record) => {
            for (const node of record.addedNodes) {
              nodes.push(node);
            }
          });

          const markdownNodes = nodes.filter((node) => {
            return node.class.contains("jp-MarkdownCell");
          }).forEach((node) => {
            typesetCellObserver.observe(node, { childList: true, subtree: true });
          });
          
        });

        const nbContainer = document.querySelector('.jp-Notebook');
        if (nbContainer !== null) {
          containerObserver.observe(nbContainer, { childList: true });
        }

        const mathEls = document.body.querySelectorAll('.quarto-inline-math, .quarto-display-math');
        return typesetMath([...mathEls]).then(() => {
          for (const mathEl of mathEls) {
            typesetCellObserver.observe(mathEl.parentElement, { childList: true, subtree: true });
          }    
        });
      });
    },
  }
};`;
                    document.head.appendChild(configEl);
                    const polyFillEl = document.createElement("script");
                    polyFillEl.setAttribute("src", "https://polyfill.io/v3/polyfill.min.js?features=es6");
                    document.head.appendChild(polyFillEl);
                    const scriptEl = document.createElement("script");
                    scriptEl.id = mathjaxId;
                    scriptEl.setAttribute("src", "https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js");
                    document.head.appendChild(scriptEl);
                }
                return Promise.resolve();
            }
        }
    }
});
/*
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

*/ 


/***/ }),

/***/ "./lib/providers/mermaid.js":
/*!**********************************!*\
  !*** ./lib/providers/mermaid.js ***!
  \**********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "mermaid": () => (/* binding */ mermaid)
/* harmony export */ });
/* harmony import */ var _plugins_mermaid__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../plugins/mermaid */ "./lib/plugins/mermaid/index.js");
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* mermaid.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/


const mermaid = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({ id: '@quarto/mermaid',
    title: 'Mermaid',
    plugin: async () => {
        // Figure out whether this is dark mode
        const isDark = document.body.getAttribute("data-jp-theme-light") === "false";
        return [_plugins_mermaid__WEBPACK_IMPORTED_MODULE_1__["default"], { dark: isDark }];
    } });


/***/ }),

/***/ "./lib/providers/provider.js":
/*!***********************************!*\
  !*** ./lib/providers/provider.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "markdownItExtension": () => (/* binding */ markdownItExtension)
/* harmony export */ });
/* harmony import */ var _const__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../const */ "./lib/const.js");

function markdownItExtension(provider) {
    return {
        id: `${_const__WEBPACK_IMPORTED_MODULE_0__.kPackageNamespace}:${provider.id}`,
        autoStart: true,
        requires: [_const__WEBPACK_IMPORTED_MODULE_0__.kMarkdownItMgr],
        activate: (_app, manager) => {
            console.log(`Quarto MarkdownIt plugin ${provider.id} is activated!`);
            manager.registerPlugin(provider);
        }
    };
}


/***/ }),

/***/ "./lib/providers/shortcodes.js":
/*!*************************************!*\
  !*** ./lib/providers/shortcodes.js ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "shortcodes": () => (/* binding */ shortcodes)
/* harmony export */ });
/* harmony import */ var _plugins_shortcodes__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../plugins/shortcodes */ "./lib/plugins/shortcodes.js");
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* shortcodes.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/


const shortcodes = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/shortcode',
    title: 'Shortcodes',
    plugin: async () => {
        return [_plugins_shortcodes__WEBPACK_IMPORTED_MODULE_1__.shortcodePlugin];
    }
});


/***/ }),

/***/ "./lib/providers/spans.js":
/*!********************************!*\
  !*** ./lib/providers/spans.js ***!
  \********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "spans": () => (/* binding */ spans)
/* harmony export */ });
/* harmony import */ var _plugins_spans__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../plugins/spans */ "./lib/plugins/spans.js");
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* spans.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/


const spans = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/spans',
    title: 'Pandoc bracketed spans',
    plugin: async () => {
        return [_plugins_spans__WEBPACK_IMPORTED_MODULE_1__.spansPlugin];
    },
});


/***/ }),

/***/ "./lib/providers/sub.js":
/*!******************************!*\
  !*** ./lib/providers/sub.js ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "sub": () => (/* binding */ sub)
/* harmony export */ });
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* sub.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/

const sub = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/sub',
    title: 'Subscript Text',
    plugin: async () => {
        const plugin = await __webpack_require__.e(/*! import() */ "webpack_sharing_consume_default_markdown-it-sub_markdown-it-sub").then(__webpack_require__.t.bind(__webpack_require__, /*! markdown-it-sub */ "webpack/sharing/consume/default/markdown-it-sub/markdown-it-sub", 23));
        return [plugin.default];
    }
});


/***/ }),

/***/ "./lib/providers/sup.js":
/*!******************************!*\
  !*** ./lib/providers/sup.js ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "sup": () => (/* binding */ sup)
/* harmony export */ });
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* sup.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/

const sup = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/sup',
    title: 'Superscript Text',
    plugin: async () => {
        const plugin = await __webpack_require__.e(/*! import() */ "webpack_sharing_consume_default_markdown-it-sup_markdown-it-sup").then(__webpack_require__.t.bind(__webpack_require__, /*! markdown-it-sup */ "webpack/sharing/consume/default/markdown-it-sup/markdown-it-sup", 23));
        return [plugin.default];
    }
});


/***/ }),

/***/ "./lib/providers/table-captions.js":
/*!*****************************************!*\
  !*** ./lib/providers/table-captions.js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "tableCaptions": () => (/* binding */ tableCaptions)
/* harmony export */ });
/* harmony import */ var _plugins_table_captions__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../plugins/table-captions */ "./lib/plugins/table-captions.js");
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* table-captions.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/


const tableCaptions = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/tableCaptions',
    title: 'Quarto Table Captions',
    plugin: async () => {
        return [_plugins_table_captions__WEBPACK_IMPORTED_MODULE_1__.tableCaptionPlugin];
    }
});


/***/ }),

/***/ "./lib/providers/tasklists.js":
/*!************************************!*\
  !*** ./lib/providers/tasklists.js ***!
  \************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "tasklists": () => (/* binding */ tasklists)
/* harmony export */ });
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* tasklists.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/

const tasklists = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/tasklists',
    title: 'Task Lists',
    plugin: async () => {
        const plugin = await __webpack_require__.e(/*! import() */ "webpack_sharing_consume_default_markdown-it-task-lists_markdown-it-task-lists").then(__webpack_require__.t.bind(__webpack_require__, /*! markdown-it-task-lists */ "webpack/sharing/consume/default/markdown-it-task-lists/markdown-it-task-lists", 23));
        return [plugin.default];
    }
});


/***/ }),

/***/ "./lib/providers/yaml.js":
/*!*******************************!*\
  !*** ./lib/providers/yaml.js ***!
  \*******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "yaml": () => (/* binding */ yaml)
/* harmony export */ });
/* harmony import */ var _plugins_yaml__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../plugins/yaml */ "./lib/plugins/yaml.js");
/* harmony import */ var _provider__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./provider */ "./lib/providers/provider.js");
/*
* yaml-block.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/


const yaml = (0,_provider__WEBPACK_IMPORTED_MODULE_0__.markdownItExtension)({
    id: '@quarto/yaml',
    title: 'Quarto Yaml',
    plugin: async () => {
        return [_plugins_yaml__WEBPACK_IMPORTED_MODULE_1__.yamlPlugin];
    }
});


/***/ }),

/***/ "./lib/widgets.js":
/*!************************!*\
  !*** ./lib/widgets.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "RenderedMarkdown": () => (/* binding */ RenderedMarkdown)
/* harmony export */ });
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/rendermime */ "webpack/sharing/consume/default/@jupyterlab/rendermime");
/* harmony import */ var _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0__);
/*
* widgets.ts
*
* Copyright (C) 2020-2023 Posit Software, PBC
*
*/

// A mime rendered that renders Quarto Markdown
class RenderedMarkdown extends _jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0__.RenderedHTMLCommon {
    constructor(options, manager) {
        super(options);
        this.renderer = null;
        this.addClass('quarto-rendered-md');
        this.markdownItManager = manager;
    }
    // Renders a mime model
    async render(model) {
        if (this.renderer === null) {
            this.renderer = await this.markdownItManager.getRenderer(this, {});
        }
        const { host, source, renderer, ...others } = {
            host: this.node,
            source: String(model.data[this.mimeType]),
            trusted: model.trusted,
            resolver: this.resolver,
            sanitizer: this.sanitizer,
            linkHandler: this.linkHandler,
            shouldTypeset: this.isAttached,
            renderer: this.renderer,
            latexTypesetter: this.latexTypesetter
        };
        // Transform source
        const markup = await renderer.preParse(source);
        // Clear the content if there is no source.
        if (!markup) {
            host.textContent = '';
            return;
        }
        // Render HTML.
        await (0,_jupyterlab_rendermime__WEBPACK_IMPORTED_MODULE_0__.renderHTML)({
            host,
            source: renderer.render(markup),
            ...others,
            shouldTypeset: false
        });
        await renderer.postRender(host);
    }
    /**
     * A message handler invoked on an `'after-attach'` message.
     */
    onAfterAttach(msg) {
        // Don't render math automatically
        // if (this.latexTypesetter ) {
        //   this.latexTypesetter.typeset(this.node);
        // }
    }
}


/***/ }),

/***/ "./style/index.css":
/*!*************************!*\
  !*** ./style/index.css ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! !../../../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "../../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_cjs_js_index_css__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! !!../../../node_modules/css-loader/dist/cjs.js!./index.css */ "../../node_modules/css-loader/dist/cjs.js!./style/index.css");

            

var options = {};

options.insert = "head";
options.singleton = false;

var update = _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default()(_node_modules_css_loader_dist_cjs_js_index_css__WEBPACK_IMPORTED_MODULE_1__["default"], options);



/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (_node_modules_css_loader_dist_cjs_js_index_css__WEBPACK_IMPORTED_MODULE_1__["default"].locals || {});

/***/ })

}]);
//# sourceMappingURL=lib_index_js.04fa35d2209ce53d4947.js.map