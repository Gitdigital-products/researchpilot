import sys, json, argparse; from pathlib import Path; from researchpilot import __version__
def build_parser():
    p = argparse.ArgumentParser(prog="researchpilot", description="ResearchPilot - AI Research Assistant")
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = p.add_subparsers(dest="command")
    sub.add_parser("review", help="Automated literature review").add_argument("path", nargs="?", default=".")
    sub.add_parser("extract", help="Extract key findings from papers").add_argument("path")
    sub.add_parser("synthesize", help="Synthesize research findings").add_argument("path")
    sub.add_parser("reproducibility", help="Check research reproducibility").add_argument("path", nargs="?", default=".")
    sub.add_parser("compliance", help="Check FAIR data compliance").add_argument("path", nargs="?", default=".")
    sub.add_parser("citations", help="Analyze citation networks").add_argument("path")
    return p
def main(argv=None):
    args = build_parser().parse_args(argv)
    if not args.command:
        build_parser().print_help(); return 0
    if args.command == "review":
        from researchpilot.analyzers.literature import LiteratureAnalyzer
        result = LiteratureAnalyzer().analyze(Path(args.path))
        print(json.dumps(result, indent=2))
        return 0
    elif args.command == "extract":
        from researchpilot.analyzers.extractor import FindingExtractor
        result = FindingExtractor().extract(Path(args.path))
        print(json.dumps(result, indent=2))
        return 0
    elif args.command == "synthesize":
        from researchpilot.analyzers.synthesizer import Synthesizer
        result = Synthesizer().synthesize(Path(args.path))
        print(json.dumps(result, indent=2))
        return 0
    elif args.command == "reproducibility":
        from researchpilot.analyzers.reproducibility import ReproducibilityChecker
        result = ReproducibilityChecker().check(Path(args.path))
        for c in result["checks"]:
            s = "PASS" if c["passed"] else "FAIL"
            print(f"  [{s}] {c['name']}: {c['detail']}")
        return 0 if result["passed"] else 1
    elif args.command == "compliance":
        from researchpilot.compliance.fair_check import FAIRCheck
        result = FAIRCheck().check(Path(args.path))
        for c in result["checks"]:
            s = "PASS" if c["passed"] else "FAIL"
            print(f"  [{s}] {c['standard']}: {c['detail']}")
        return 0 if result["passed"] else 1
    elif args.command == "citations":
        from researchpilot.analyzers.citations import CitationAnalyzer
        result = CitationAnalyzer().analyze(Path(args.path))
        print(json.dumps(result, indent=2))
        return 0
if __name__ == "__main__":
    sys.exit(main())
